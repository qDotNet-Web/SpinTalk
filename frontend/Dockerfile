FROM oven/bun:alpine AS build

WORKDIR /app

COPY package*.json bun.lockb /app/

RUN bun install

COPY . .

RUN bun run build

FROM oven/bun:alpine

WORKDIR /app

COPY --from=builder /app /app

EXPOSE 80

CMD ["bun", "run", "start"]