# develop stage
FROM node:16-alpine3.11 as develop-stage 

WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH
COPY package.json /app/package.json

RUN yarn install
RUN yarn add @vue/cli
RUN yarn add vuex
RUN yarn add vue-router
RUN yarn add axios
RUN yarn add vue-axios
RUN yarn add bootstrap
RUN yarn add nodemon
RUN yarn add firebase
RUN yarn add cors
RUN yarn add @nuxtjs/vuetify -D
RUN yarn add vuetify
RUN yarn add bootstrap b
RUN yarn add bootstrap-vue 
RUN yarn add popper.js
RUN yarn add utf-8-validate@^5.0.2
RUN yarn add bufferutil@^4.0.1
COPY . . 

CMD ["yarn", "serve"]

# build stage
#FROM develop-stage as build-stage
#RUN yarn build