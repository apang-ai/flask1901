<template>
    <div class='index-wrapper'>
        <div class='index-left'>
            <div class="index-left-block all-products">
                <h2>全部产品</h2>
                <template v-for='product in productList'>
                    <h3>{{ product.title }}</h3>
                    <ul>
                        <li v-for='item in product.list'>
                            <a v-bind:href="item.url">{{ item.title }}</a>
                            <span v-if='item.hot' class='hot-tag'>HOT</span>
                        </li>
                    </ul>
                    <hr v-if='!product.last'/>                        
                </template>
                <!-- <ul>
                    <li v-for='item in productList.pc.list'>
                        <a v-bind:href="item.url">{{ item.title }}</a>
                    </li>
                </ul> -->
                
                <!-- <h3>手机应用类</h3>
                <ul>
                    <li v-for='item in productList.app.list'>
                        <a v-bind:href="item.url">{{ item.title }}</a>
                    </li>
                </ul> -->
            </div>
            <div class="index-left-block lastest-news">
                <h2>最新消息</h2>
                <ul v-for='msg in newmsgs.list'>
                    <li>
                        <a v-bind:href="msg.url">{{ msg.title }}</a>
                    </li>
                </ul>
            </div>
        </div>
        <div class='index-right'>
            <div style='width: 900px; height:300px; margin: 0 auto; background: red;'>slider</div>
            <div class='index-board-list'>
                <div class='index-board-item' v-for='item in gongneng.list'>
                    <img :src='item.imgurl' alt="">
                    <div class='index-board-item-inner'>
                        <h2>{{ item.title }}</h2>
                        <p>{{ item.content }}</p>
                        <div class='index-board-button'>立即购买</div>
                    </div>
                </div>
                <!-- <div class='index-board-item'>
                    <img src="" alt="">
                    <div class='index-board-item-inner'>
                        <h2>戴尔电脑</h2>
                        <p>戴尔电脑就是好</p>
                        <div class='index-board-button'>立即购买</div>
                    </div>
                </div> -->
                <!-- <div class='index-board-item'>
                    <img src="../assets/car.png" alt="">
                    <div class='index-board-item-inner'>
                        <h2>戴尔电脑</h2>
                        <p>戴尔电脑就是好</p>
                        <div class='index-board-button'>立即购买</div>
                    </div>
                </div>
                <div class='index-board-item'>
                    <img src="../assets/jinzita.png" alt="">
                    <div class='index-board-item-inner'>
                        
                        <h2>戴尔电脑</h2>
                        <p>戴尔电脑就是好</p>
                        <div class='index-board-button'>立即购买</div>
                    </div>
                </div> -->
                
            </div>
        </div>
        
    </div>
</template>

<script>
export default {
    data:function(){

        return {
            productList: {
                pc: {
                    title: "PC产品",
                    list: [
                    {
                        title: "数据统计",
                        url: "http://starcraft.com"
                    },
                    {
                        title: "数据预测",
                        url: "http://warcraft.com"
                    },
                    {
                        title: "流量分析",
                        url: "http://overwatch.com",
                        hot: true
                    },
                    {
                        title: "广告发布",
                        url: "http://hearstone.com"
                    }   
                    ]
                },
                app: {
                    title: "手机应用类",
                    last: true,
                    list: [
                    {
                      title: "91助手",
                      url: "http://weixin.com"
                    },
                    {
                      title: "产品助手",
                      url: "http://weixin.com",
                    hot:true
                    },
                    {
                      title: "智能地图",
                      url: "http://maps.com"
                    },
                    {
                      title: "语音助手",
                      url: "http://phone.com",
                    hot:true
                    }
                  ]
                }
            },
            newmsgs: {
                list: [
                    {
                        title: '杨坤diss惊雷',
                        url:'https://baijiahao.baidu.com/s?id=1664030735516530339&wfr=spider&for=pc'
                    },
                    {
                        title: '新冠病毒最新消息',
                        url: 'http://www.stdaily.com/index/kejixinwen/2020-04/15/content_921587.shtml'
                    },
                    {
                        title: '华为手机市场营销',
                        url: 'https://baijiahao.baidu.com/s?id=1636635866999933325&wfr=spider&for=pc'
                    },
                    {
                        title: '苹果手机最新动态',
                        url: 'https://baijiahao.baidu.com/s?id=1662192615793738692&wfr=spider&for=pc'
                    }
                ]

            },
            gongneng: {
                list: [
                    {
                        imgurl: '../src/assets/diqiu.png',
                        title: '其共识会',
                        content: '离委离究能族管观',
                    },
                    {
                        imgurl: '../src/assets/laba.png',
                        title: '认该学温',
                        content: '处做一贯神作大号当前',
                    },
                    {
                        imgurl: '../src/assets/car.png',
                        title: '飞政与将',
                        content: '给组织实缴大活动空',
                    },
                    {
                        imgurl: '../src/assets/jinzita.png',
                        title: '走把钱多',
                        content: '立管体站市二院打开了',
                    }
                ]
            }
        }

    }
}
</script>

<style scoped>
    .index-wrapper{
        width: 1200px;
        margin: 0 auto;
        display: flex;
    }
    .index-left{
        width: 300px;
    }
    .index-right{
        width: 900px;
    }
    .index-left-block{
        margin: 15px;
        background: #ffffff;
        box-shadow: 0 0 1px #ddd;
        border-radius: 0 0 10px 10px;
    }
    .index-left-block h2{
        color: #ffffff;
        background: #4fc08d;
        padding: 10px 15px;
        margin-bottom: 15px;
    }
    .all-products h3{
        padding: 0 15px 5px 15px;
        font-weight: bolder;
        color: #222;
        /* margin-bottom: 15px; */
    }
    .index-left-block ul{
        padding: 10px 15px;
    }
    .index-left-block ul li{
        padding: 5px;
    }
    .hot-tag{
        color: white;
        background: purple;
        font-size: 13px;
    }
    .index-board-list{
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;
    }
    .index-board-item{
        width: 400px;
        background: #ffffff;
        box-shadow: 0 0 1px #ddd;
        margin-bottom: 20px;
        padding-top: 20px;
    }
    .index-board-item-inner{
        height: 125px;
        padding-left: 120px;
        /* background: url('../assets/car.png') no-repeat; */
    }
    .index-board-item-inner h2{
        font-size: 18px;
        font-weight: bolder;
        color: #000000;
        margin-bottom: 15px;
    }
    .index-board-item-inner p{
        margin-bottom: 15px;
    }
    .index-board-button{
        width: 80px;
        height: 40px;
        line-height: 40px;
        background: limegreen;
        color: #fff;
        border-radius: 5px;
        text-align: center;
        cursor: pointer;
    }
    .index-board-item img{
        position: absolute;
    }
</style>