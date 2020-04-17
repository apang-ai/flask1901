<template>
    <div class='slider-warpper' @mouseover="clearInv" @mouseout="runInv">
        <!-- 轮播图区域 -->
        <div v-show='index===nowIndex' v-for='(item, index) in sliderImageList' :key='index' class="slider-item" v-bind:class='["item"+[index+1]]'>
            <a href="">
                <img v-bind:src=item.imgurl alt="">
            </a>
        </div>
        <!-- 图片标题 -->
        <h2 class='slider-title'>{{ sliderImageList[nowIndex].title }}</h2>
        <!-- 上一张下一张 -->
        <a v-on:click='preHandler' href="javascript:void(0)" class='btn pre-btn'>&lt;</a>
        <a v-on:click='nextHandler' href="javascript:void(0)" class='btn next-btn'>&gt;</a>
        <!-- dots -->
        <ul class='slider-dots'>
            <li v-on:click='clickDots(index)' v-for='(item,index) in sliderImageList' :kye="index">{{ index+1 }}</li>
        </ul>
    </div>
</template>

<script>
export default {
    data() {
        return {
            nowIndex:0,
            sliderImageList: [
                {
                    title:'第一张',
                    imgurl:require('../assets/logo1.png')
                },
                {
                    title:'第二张',
                    imgurl:require('../assets/logo2.png')
                },
                {
                    title:'第三张',
                    imgurl:require('../assets/logo3.png')
                },
                {
                    title:'第四张',
                    imgurl:require('../assets/logo4.png')
                },

            ]
        }
    },
    methods: {
        clickDots(index){
            this.nowIndex = index
            console.log(this.nowIndex)
        },
        preHandler(){
            this.nowIndex--;
            if(this.nowIndex<0){
                this.nowIndex=3
            }
        },
        nextHandler(){
            // console.log(this.nowIndex)
            this.autoPlay()
        },
        autoPlay(){
            this.nowIndex++;
            if(this.nowIndex > 3){
                this.nowIndex = 0
            }
        },
        runInv(){
            this.invId = setInterval(this.autoPlay,2000)
        },
        clearInv(){
            clearInterval(this.invId)
        },

    },
    created() {
        this.runInv()
    },
}
</script>

<style>
    .slider-warpper{
        width: 900px;
        height: 500px;
        overflow: hidden;
        position: relative;
        margin-top: 14px;
    }
    .slider-item{
        width: 900px;
        height: 500px;
        position: absolute;
    }
    .item1{
        z-index: 100;
    }
    .item2{
        z-index: 90;
    }
    .item3{
        z-index: 80;
    }
    .item4{
        z-index: 70;
    }
    .slider-dots{
        position: absolute;
        right: 50px;
        bottom: 10px;
        z-index: 200;
    }
    .slider-dots li{
        width: 20px;
        height: 20px;
        background: black;
        float: left;
        border-radius: 50%;
        text-align: center;
        line-height: 20px;
        color: white;
        opacity: 0.6;
        margin: 0 10px;
        cursor: pointer;
    }
    .btn{
        width: 50px;
        height: 70px;
        background: #000;
        color: #ffffff;
        position: absolute;
        z-index: 300;
        top: 50%;
        margin-top: -35px;
        font-size: 40px;
        line-height: 65px;
        text-align: center;
        opacity: 0.65;
    }
    .pre-btn{
        left: 10px;
    }
    .next-btn{
        right: 10px;
    }
    .slider-title{
        position: absolute;
        z-index: 400;
        color: #ffffff;
        width: 100px;
        height: 40px;
        left: 10px;
        font-size: 18px;
        background: #000;
        opacity: 0.65;
        line-height: 40px;
    }
</style>