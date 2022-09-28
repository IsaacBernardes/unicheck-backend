FROM node:16.17.1-alpine
RUN apk update \
    apk add \
    build-base \
    libpq
RUN mkdir /app
WORKDIR /app
COPY . .
RUN npm install
