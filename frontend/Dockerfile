FROM jarredsumner/bun:edge AS build

WORKDIR /app

COPY package*.json bun.lockb /app/

RUN bun install

COPY . .

RUN bun run build

FROM jarredsumner/bun:edge

WORKDIR /app

COPY --from=builder /app /app

EXPOSE 80

CMD ["bun", "run", "start"]