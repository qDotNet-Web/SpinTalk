const signalingServerUrl = 'wss://your-signaling-server-url'; // Replace with your signaling server URL
let localPeerConnection: RTCPeerConnection;
let remotePeerConnection: RTCPeerConnection;
let localStream: MediaStream;
let remoteStream: MediaStream;
let signalingSocket: WebSocket;

const configuration = {
	iceServers: [
		{ urls: 'stun:stun.l.google.com:19302' },
		{ urls: 'stun:stun1.l.google.com:19302' },
		{ urls: 'stun:stun2.l.google.com:19302' },
		{ urls: 'stun:stun3.l.google.com:19302' },
		{ urls: 'stun:stun4.l.google.com:19302' }
	]
};

async function startWebRTC() {
	// Initialize WebSocket for signaling
	signalingSocket = new WebSocket(signalingServerUrl);

	signalingSocket.onmessage = async (message) => {
		const data = JSON.parse(message.data);

		if (data.type === 'offer') {
			await handleOffer(data.offer);
		} else if (data.type === 'answer') {
			await handleAnswer(data.answer);
		} else if (data.type === 'candidate') {
			await handleCandidate(data.candidate);
		}
	};

	// Create RTCPeerConnection for local and remote peers with STUN servers
	localPeerConnection = new RTCPeerConnection(configuration);
	remotePeerConnection = new RTCPeerConnection(configuration);

	// Get user media
	localStream = await navigator.mediaDevices.getUserMedia({ video: true });
	// document.querySelector('#video-other').srcObject = localStream;

	// Add local stream to local peer connection
	localStream.getTracks().forEach(track => localPeerConnection.addTrack(track, localStream));

	// Handle ICE candidates
	localPeerConnection.onicecandidate = (event) => {
		if (event.candidate) {
			signalingSocket.send(JSON.stringify({ type: 'candidate', candidate: event.candidate }));
		}
	};

	remotePeerConnection.onicecandidate = (event) => {
		if (event.candidate) {
			signalingSocket.send(JSON.stringify({ type: 'candidate', candidate: event.candidate }));
		}
	};

	// Handle remote stream
	remotePeerConnection.ontrack = (event) => {
		if (!remoteStream) {
			remoteStream = new MediaStream();
			// document.querySelector('#video-self').srcObject = remoteStream;
		}
		remoteStream.addTrack(event.track);
	};

	// Create and send offer
	const offer = await localPeerConnection.createOffer();
	await localPeerConnection.setLocalDescription(offer);
	signalingSocket.send(JSON.stringify({ type: 'offer', offer }));
}

async function handleOffer(offer: RTCSessionDescriptionInit) {
	await remotePeerConnection.setRemoteDescription(new RTCSessionDescription(offer));
	const answer = await remotePeerConnection.createAnswer();
	await remotePeerConnection.setLocalDescription(answer);
	signalingSocket.send(JSON.stringify({ type: 'answer', answer }));
}

async function handleAnswer(answer: RTCSessionDescriptionInit) {
	await localPeerConnection.setRemoteDescription(new RTCSessionDescription(answer));
}

async function handleCandidate(candidate: RTCIceCandidateInit) {
	const iceCandidate = new RTCIceCandidate(candidate);
	await localPeerConnection.addIceCandidate(iceCandidate);
	await remotePeerConnection.addIceCandidate(iceCandidate);
}

// Start WebRTC connection
startWebRTC();