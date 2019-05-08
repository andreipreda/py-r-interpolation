const express = require('express')
const compression = require('compression')
const helmet = require('helmet')
const proxy = require('http-proxy-middleware')

const app = express()
app.use(helmet())
app.use(compression())
app.use(express.static(process.env.STATIC_APP || './static'))

app.use(
  '/api',
  proxy({ 
    target: process.env.FLASK_ENDPOINT || 'http://0.0.0.0:7000',
    changeOrigin: true,
    protocolRewrite: true })
);

app.get('/', (_, res) => {
  res.sendFile('index.html', { root: process.env.STATIC_APP || 'static' })
})

const port = process.env.EXPRESS_PORT || '8080'
app.listen(port, () => console.log(`Express running on ${port}`))