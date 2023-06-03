const axios = require("axios");
const API_KEY = 'AIzaSyADsnz4yXpvHuN4DSOt815JXiy_BgHGlrk';
const { Configuration, OpenAIApi } = require("openai");
const sendData = async (arrayToSend) => {
    try {
      const response = await axios.post('http://127.0.0.1:5000', {
        array: arrayToSend,
      });
      console.log('Array sent successfully');
      console.log('Response:', response.data[0][0]); // Process the response data as needed
      FinalData=response.data[0][0]
    } catch (error) {
      console.error('Error sending array:', error);
    }
  };
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

//OPENAI_API_KEY='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';
//OPENAI_API_KEY='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';
//OPENAI_API_KEY='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';
OPENAI_API_KEY='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';

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

  module.exports = {
    sendData,
    sendData1,
    searchYouTube,
    runCompletion
  };