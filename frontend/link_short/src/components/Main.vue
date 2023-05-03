<template>
  <div class="hello">
  <H1>Короткие ссылки</H1>
  <h3>Введите ссылку</h3>  
  <div><input type="text" size="50" v-model="this.text_long_link" /></div>
  <br>
  <button @click="get_short_link">Сгенерировать</button>
  <h3>Коротка ссылка:</h3>
  <div>{{short_link}}</div>

  <br>
  <div><button @click="copyToClipBoard">Скопировать</button></div>
  </div>
</template>

<script>
import axios from 'axios'
console.log(import.meta.env)
export default {
  name: "ShortLink",
  data() {
    return {
      url: import.meta.env.VITE_URL_BACK,
      short_link: "",
      text_long_link: ""
    }
  },
  methods:{
    good(response){
      console.log('Ответ сервера успешно получен!');
              if (response.data.ERROR){
                this.short_link=response.data.ERROR;
              }
              else{
                localStorage[this.text_long_link] = window.location.href + response.data.response;
                this.short_link=window.location.href + response.data.response;
              }
              console.log('Ответ сервера успешно получен!');
              console.log(response.data);
    },
    set_short_link(text){
      this.short_link = text
    },
    get_short_link()
    {
      if (this.text_long_link == "")
      {
        alert("Введите ссылку.")
        return
      }
      this.short_link = "Запрос ссылки..."
      if (localStorage[this.text_long_link]) {
        this.short_link = localStorage[this.text_long_link];
      }
      else{
        try{
            axios({
            method:"POST",
            url: '/api/get_short_link',
            data:{
              link: this.text_long_link
            },
            headers: {
                "Content-type": "application/json; charset=UTF-8"
              }
          }).then(this.good).error(function(error) {
              console.log(error);
            }
            );
        }
        catch(exceptionVar){
          this.short_link = "Сервер не доступен.";
          console.log(exceptionVar);
        }   
      }
    },
    copyToClipBoard(){
      window.navigator.clipboard.writeText(this.short_link)
      
    }
  }
  
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
