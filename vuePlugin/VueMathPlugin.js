export default{
    install:function(Vue){
        // 求一个值的平方
        Vue.directive('square', function(el, binding){    
            el.innerHTML = Math.pow(binding.value, 2)
        });
        // 开方
        Vue.directive('sqrt', function(el,binding){
            el.innerHTML = Math.sqrt(binding.value)
        })
        // sin值
        Vue.directive('sin', function(el, binding){
            el.innerHTML = Math.sin(binding.value)
        })
        // cos值
        Vue.directive('cos', function(el, binding){
            el.innerHTML = Math.cos(binding.value)
        })
        // tan值
        Vue.directive('tan', function(el, binding){
            el.innerHTML = Math.tan(binding.value)
        })
    }
}