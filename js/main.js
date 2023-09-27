const express = require('express');
const mysql = require('mysql');

const app = express();

const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  port: 3308,
  password: '',
  database: 'bigdata'
});

connection.connect();

app.get('/data', (req, res) => {
  const query = 'SELECT * FROM data';
  connection.query(query, (error, results) => {
    if (error) throw error;
    res.json(results);
  });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});
