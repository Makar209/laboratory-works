const express = require('express');
const path = require('path');
const userRouter = require('./routes.js')

const PORT = process.env.PORT || 8080;

const app = express();

app.use(express.json())
app.use('/api', userRouter);
app.use(express.static(path.resolve(__dirname, 'pages')))

app.listen(PORT, () => console.log(`server started on ${PORT}`));


