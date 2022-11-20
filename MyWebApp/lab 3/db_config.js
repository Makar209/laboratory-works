const Pool = require('pg').Pool;

const pool = new Pool( {
    user: "postgres",
    password: "1703", 
    host: "localhost",
    port: 5432,
    database: "service_db",

} )

module.exports = pool;