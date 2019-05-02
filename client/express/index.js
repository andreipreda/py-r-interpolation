const express = require('express')
const compression = require('compression')
const helmet = require('helmet')

const app = express()
app.use(helmet())
app.use(compression())
app.use(express.static(process.env.APP_TO_SERVE || './static'))

app.get('*', (_, res) => {
  res.sendFile('index.html', { root: process.env.APP_TO_SERVE || 'static' })
})

const port = process.env.EXPRESS_PORT || '8080'
app.listen(port, () => console.log(`Express running on ${port}`))
