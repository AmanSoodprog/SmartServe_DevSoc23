const express = require('express');
const router = express.Router();
const axios = require("axios")
const bodyParser = require('body-parser');
router.use(bodyParser.urlencoded({ extended: true }));
const { sendData, sendData1,searchYouTube,runCompletion, Beta1 } = require('./apiFunc');


router.get('/', (req, res) => {
    res.render('Home');
});

router.get('/SelfHelp', (req, res) => {
  res.render('SelfHelp');
});

router.get('/Locate', (req, res) => {
  res.render('Locate');
});

router.get('/Sell', (req, res) => {
  res.render('Sell');
});

router.get('/PushDB', (req, res) => {
  res.render('PushDB');
});


router.get('/search', async (req, res) => {
  const searchQuery = req.query.input;
  try {
    const results = await searchYouTube(searchQuery);
    const answer = await runCompletion(searchQuery);
    const answer1 = await Beta1(searchQuery);
    console.log(answer1)
    res.render('SearchResults', { results:results,answer: answer ,answer1:answer1});
  } catch (error) {
    res.render('SearchResults', { error: 'Error fetching YouTube search results' });
  }
});

router.post('/process',async (req, res) => {
  const PhoneDet = req.body
  console.log(PhoneDet)
  const formDataArray = Object.values(PhoneDet);
  try {
    await sendData(formDataArray)
    res.render('predict',{FinalData})
  } catch (error) {
  }
});

router.post('/pushDB', async(req, res) => {
  const PhoneDet = req.body

  try{
    console.log(PhoneDet)
    await sendData1(PhoneDet)
    res.render('PushDB')
  } catch (error) {
  }
});

module.exports = router;
