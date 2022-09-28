FROM node:16.17.1-alpine
RUN apk update \
    apk add \
    build-base \
    postgresql \
    postgresql-dev \
    libpq
RUN mkdir /app
WORKDIR /app
COPY . .
COPY ./server/infra/database-prod.js ./server/infra/database.js
RUN npm install
