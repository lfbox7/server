const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const cors = require('cors');

require('dotenv').config();

// routers
const routes = require('./routes/routes');

// middleware applications
const app = express();
app.use(express.static(path.join(__dirname, 'client/build')));
app.use(
    bodyParser.urlencoded({
        extended: true,
    })
);
app.use(bodyParser.json());
app.use(cors());
app.use('/', routes);

app.listen(process.env.PORT, () => {
    console.log('Express server is running!');
});