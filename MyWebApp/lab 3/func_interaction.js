const { application } = require("express");
const db = require('./db_config.js')

class Controller {
    async createUser(req, res) {
        const {full_name, login, password} = req.body;
        const newPerson = await db.query(`INSERT INTO service_users (full_name, login, password) values($1, $2, $3) RETURNING *`, [full_name, login, password]);
        console.log(newPerson.rows[0]);
        res.json(newPerson.rows[0]);
    }
    async getUser(req, res) {
        const login = req.params.login;
        const password = req.params.password;
        const user = await db.query(`SELECT * FROM service_users WHERE login = $1 AND password = $2`, [login, password]);
        //console.log(user);
        res.json(user.rows[0]);
    }
    async updateUser(req, res) {

    }
    async deleteUser(req, res) {

    }

}

module.exports = new Controller;