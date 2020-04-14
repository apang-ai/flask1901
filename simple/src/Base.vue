<template>
  <div id="app">
    <h1 class='base-h1'>{{ msg }}</h1>
    <div class='app-heard'>
      <Header/>
    </div>
    <div class='app-content'>
      <Content/>
    </div>
    <div class='app-footer'>
      <Footer/>
    </div>
    <HelloComponent/>
  </div>
</template>

<script>
import Header from './components/Header'
import Content from './components/Content'
import Footer from './components/Footer'

export default {
  data(){
    return {
      msg: '基础模板'
    }
  },
  components: {
    Header,
    Content,
    Footer
  }
}
</script>

<style>
.base-h1 {
  color: red;
}
</style>
