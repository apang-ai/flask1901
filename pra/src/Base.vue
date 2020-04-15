<template>
  <div id="app">
    
    <div class='com-heard'>
      <Header/>
    </div>
    <div class='com-content'>
      <Content/>
    </div>
    <div class='com-footer'>
      <Footer/>
    </div>
  </div>
</template>

<script>
import Header from './components/Header'
import Content from './components/Content'
import Footer from './components/Footer'

export default {
  
  components: {
    Header,
    Content,
    Footer
  }
}
</script>

<style>
*{
  margin: 0;
  padding: 0;
  list-style: none;
  text-decoration: none;
}
#app{
  height: 100%;
  background: whitesmoke;
}
.com-header{
  width: 100%;
  height: 60px;
  background: rgba(0, 0, 0, 0.678);
}
.com-header-box{
  position: relative;
  width: 1000px;
  height: 60px;
  margin: 0 auto;
  /* background: rgba(0, 0, 0, 0.678); */
}
.header-img{
  float: left;
  position: absolute;
  top: 10px;
}
.header-ul{
  /* width: 300px; */
  line-height: 30px;
  float: right;
}
.header-ul li{
  float: left;
  margin: 15px;
}
.header-ul li a{
  color: white;
  font-size: 15px;
}
.header-sp1{
  position: absolute;
  left: 879px;
  top: 14px;
}
.header-sp2{
  position: absolute;
  left: 938px;
  top: 14px;
}
.com-content{
  position: relative;
  width: 1000px;
  height: 780px;
  background: #f8f8f8;
  margin: 0 auto;
  
}
.content-all-shop{
  position: absolute;
  top: 20px;
  width: 220px;
  height: 362px;
  background: rgba(255, 255, 255, 0.93);
  border: solid 1px rgba(255, 255, 255, 0.93);
  box-shadow: 0px 1px 3px -2px #222121;
  border-bottom-right-radius: 10px;
  border-bottom-left-radius: 10px;

}
.content-sp{
    width: 200px;
    height: 40px;
    background: rgba(41, 209, 63, 0.747);
    color: white;
    display: block;
    font-size: 15px;
    line-height: 40px;
    text-align: 16px;
    padding: 0 10px;
}
.content-p{
    width: 200px;
    height: 50px;
    padding: 0 10px;
    line-height: 50px;
    font-size: 15px;
}
.content-ul-pc{
  width: 180px;
  padding: 0 20px;
}
.content-ul-pc li{
  margin: 5px 0;
}
.content-ul-pc li a{
  font-size: 15px;
  color: black;
}
.content-box-ul{
  width: 220px;
  height: 105px;
  border-bottom: solid 1px #a7a4a4fa;
}
.content-box-ul-phone{
  width: 220px;
  height: 105px;
}
.content-all-msg{
  position: absolute;
  top: 396px;
  width: 220px;
  height: 362px;
  background: rgba(255, 255, 255, 0.93);
  border: solid 1px rgba(255, 255, 255, 0.93);
  box-shadow: 0px 1px 3px -2px #222121;
  border-bottom-right-radius: 10px;
  border-bottom-left-radius: 10px;

}
.content-ul-msg{
  margin: 30px 0;
  width: 180px;
  padding: 0 20px;
}
.content-ul-msg li{
  margin: 5px 0;
}
.content-ul-msg li a{
  font-size: 15px;
  color: black;
}
.com-footer{
    width: 1000px;
    height: 60px;
    background: rgba(231, 231, 231, 0.42);
    margin: 0 auto;
    text-align: center;
    line-height: 60px;
}
.content-img-login{
  position: absolute;
  width: 700px;
  height: 300px;
  background: #3b51edb5;
  left: 288px;
  top: 20px;
}
.content-ul-login{
    position: absolute;
    left: 300px;
    top: 265px;
}
.content-ul-login li{
    width: 10px;
    display: block;
    height: 10px;
    background: white;
    border-radius: 10px;
    float: left;
    margin-left: 15px;
}
.content-gong{
    position: absolute;
    width: 700px;
    height: 300px;
    left: 233px;
    top: 334px;
}
.content-gong-ul{
  width: 900px;
  height: 450px;
}
.content-gong-ul li{
  position: relative;
  display: block;
  width: 320px;
  height: 160px;
  background: white;
  float: left;
  margin-left: 58px;
  margin-top: 20px;
  box-shadow: 0px 1px 3px -2px #222121;
  border-radius: 10px;
}
.content-gong-sp-img{
  position: absolute;
  left: 10px;
  top: 28px;
}
.content-gong-h{
  position: absolute;
  left: 125px;
  top: 30px
}
.content-gong-p{
  position: absolute;
  left: 125px;
  top: 70px;
}
.content-gong-btn{
  position: absolute;
  left: 125px;
  top: 110px;
  width: 80px;
  height: 40px;
  background: #60dd70;
  border: none;
  border-radius: 6px;
}
.content-gong-btn a{
  font-size: 13px;
  color: white;
}
</style>
