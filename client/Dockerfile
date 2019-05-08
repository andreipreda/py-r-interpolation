FROM node:8.16.0-alpine

RUN npm i -g @angular/cli

COPY . client

WORKDIR /client/angular

RUN npm i

RUN ng build --prod --output-path=/client/express/static

WORKDIR /client/express

RUN npm i

CMD ["node", "index.js"]
