FROM node:latest AS build

WORKDIR /BisonSpace/backend

COPY ./backend/package.json .

RUN npm i

COPY ./backend .

EXPOSE 4000