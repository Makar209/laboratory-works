const Router = require('express');
const router = new Router();
const Controller = require('./func_interaction.js');

router.post('/user', Controller.createUser);
router.get('/user/:login/:password', Controller.getUser);
router.put('/user', Controller.updateUser);
router.delete('/user', Controller.deleteUser);

module.exports = router;