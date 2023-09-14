import axios from 'axios';

var host = 'http://127.0.0.1:8000/datas/'

const instance = axios.create({
  baseURL: host, // 设置基本的API URL
  timeout: 5000, // 设置请求超时时间
});

export const getMyData = async () => {
  try {
    const response = await instance.get('hello');
    return response.data;
  } catch (error) {
    throw error;
  }
};
