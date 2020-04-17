<template>
    <div class='login-wrapper'>
        <div class='ui-mask'>
        </div> 
        <div class='ui-dialog' id='dialog'>
            <div class='ui-dialog-title'>
                用户名密码登录
                <a class='ui-dialog-closebutton' href="javascript:void(0)">×</a>
            </div>
            <div class=ui-dialog-content>
                <p style="color:red">{{ errorText }}</p>
                <div class="ui-dialog-item">
                    
                    <input v-model="usernameModel" class='ui-dialog-input' type="text" placeholder="手机/邮箱/用户名">
                </div>
                <div class="ui-dialog-item">
                    <input v-model="passwordModel" class='ui-dialog-input' type="password" placeholder="密码">
                </div>
                <div>
                    <a v-on:click='onLogin' href="javascript:void(0)" class='ui-dialog-submit'>登录</a>
                </div>
                <div class="ui-dialog-item">
                    <a href="javascript:void(0)">忘记密码</a>
                </div>
                <div class="ui-dialog-item">
                    <a href="javascript:void(0)">立即注册</a>
                </div>
            </div>
        </div>               
    </div>
</template>

<script>
export default {
    data() {
        return {
            usernameModel: '',
            passwordModel: '',
            errorText: '',
        }
    },
    computed: {
        userErrors(){
            let errorText, status;
            if(!/@/g.test(this.usernameModel)){
                status=false
                errorText = '不包含@符号'
                console.log(errorText)
            }else{
                status=true
                errorText='账号对了'
                console.log(errorText)
            }
            return {errorText, status}
        },
        passwordError(){
            let errorText, status;
            if(/^(\w){6,10}$/g.test(this.passwordModel)){
                status=false
                errorText='密码不是1-6位'
                console.log(errorText)
            }else{
                status=true
                errorText='密码对了'
                console.log(errorText)
            }
            return {errorText, status}
        },       
    },
    methods: {
            onLogin(){
                if(!this.userErrors.status || !this.passwordError.status){
                    this.errorText = '校验没通过'
                }else{
                    this.errorText=''
                    this.$http.get('api/login')
                    .then(response => {
                        this.$emit('', response.data)
                    },(error)=>{
                        console.log(error)
                    })
                }
            }
        },
}
</script>

<style scoped>
.ui-mask{
    width: 100%;
    height: 100%;
    background: #000;
    opacity: 0.45;
    position: absolute;
    top: 0;
    left: 0;
    z-index: 8000;
}
.ui-dialog{
    width: 400px;
    height: auto;
    position: absolute;
    top: 50%;
    left: 50%;
    margin-left: -200px;
    border: 1px solid #d5d5d5;
    background: #ffffff;
    z-index: 9000;

}
.ui-dialog-title{
    height: 50px;
    line-height: 50px;
    padding: 0 20px;
    color: #535353;
    font-size: 16px;
    background: #f5f5f5;
    cursor: move;
}
.ui-dialog-closebutton{
    display: block;
    width: 16px;
    height: 16px;
    position: absolute;
    top: 0;
    right: 20px;
    cursor: pointer;
}
.ui-dialog-closebutton:hover{
    color: red;
}
.ui-dialog-content{
    padding: 15px;
}
.ui-dialog-item{
    height: 40px;
    line-height: 40px;
    text-align: right;
    padding-top: 15px;
}
.ui-dialog-input{
    width: 100%;
    height: 40px;
    margin: 0px;
    padding: 0px;
    border: 1px solid #d5d5d5;
    outline: none;
    text-indent: 10px;
    color: #c1c1c1;
    font-size: 16px;
}
.ui-dialog-submit{
    display: block;
    width: 100%;
    height: 50px;
    background: #3b7ae3;
    border: none;
    outline: none;
    font-size: 16px;
    font-weight: bolder;
    text-align: center;
    line-height: 50px;
    margin-top: 20px;
    color: #ffffff;
}
.ui-dialog-submit:hover{
    background: #246ae2;
}
</style>