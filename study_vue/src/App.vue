<script setup>
import HelloWorld from './components/HelloWorld.vue'
import TheWelcome from './components/TheWelcome.vue'
</script>

<template>
  <header>
    <img alt="Vue logo" class="logo" src="./assets/logo.svg" width="125" height="125" />

    <div class="wrapper">
      <HelloWorld msg="You did it!" />
    </div>
  </header>

  <main>
    <TheWelcome />
    <h1>{{ message }}</h1>
  </main>
</template>


<script>
import { getMyData } from '@/common/api'; // 导入封装的GET请求函数

export default {
  data() {
    return {
      responseData: {
        message: '',
      },
    };
  },
  async mounted() {
    try {
      const response = await getMyData(); // 使用封装的GET请求函数
      console.log(response); // 打印响应数据到控制台
      this.responseData.message = response.message; // 更新组件数据
    } catch (error) {
      console.error(error); // 打印错误到控制台
      this.responseData.message = 'An error occurred while fetching data.'; // 更新组件数据
    }
  },
};
</script>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
