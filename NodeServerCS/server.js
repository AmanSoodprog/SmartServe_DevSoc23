const routes = require('./routes/router');
const path = require('path');
const express = require('express');
const app = express();
const port = 3001;

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));
app.use(express.static(path.join(__dirname,'views')))

app.use('/',routes)

app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
  });