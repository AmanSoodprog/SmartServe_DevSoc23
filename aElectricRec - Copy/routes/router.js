const express = require('express');
const router = express.Router();
const axios = require("axios")
const bodyParser = require('body-parser');
router.use(bodyParser.urlencoded({ extended: true }));
const { Configuration, OpenAIApi } = require("openai");

const API_KEY = 'AIzaSyADsnz4yXpvHuN4DSOt815JXiy_BgHGlrk';
//OPENAI_API_KEY='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';
OPENAI_API_KEY='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';



const sendData1 = async (arrayToSend) => {
  try {
    const response = await axios.post('http://127.0.0.1:5000/dbd', {
      array: arrayToSend,
    });
    console.log('Array sent successfully');
  } catch (error) {
    console.error('Error sending array:', error);
  }
};

const configuration = new Configuration({
  apiKey: OPENAI_API_KEY,
});
const openai = new OpenAIApi(configuration);


async function runCompletion (inp) {
  const completion = await openai.createCompletion({
  model: "text-davinci-003",
  prompt: inp,
  max_tokens:4000
  });
  return completion.data.choices[0].text;
}
  
async function searchYouTube(query) {
  const url = `https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=3&q=${encodeURIComponent(query)}&key=${API_KEY}&type=video`;
  try {
    const response = await axios.get(url);
    const data = response.data;

    return data.items;
  } catch (error) {
    console.log('Error fetching YouTube search results:', error.message);
    return [];
  }
}


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
    res.render('SearchResults', { results:results,answer: answer });
  } catch (error) {
    res.render('SearchResults', { error: 'Error fetching YouTube search results' });
  }
});

router.post('/process',async (req, res) => {
  const PhoneDet = req.body
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
