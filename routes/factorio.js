var express = require('express');
var router = express.Router();

router.get("/", function(req, res,next) {
  res.render("factorio");
});

module.exports = router;