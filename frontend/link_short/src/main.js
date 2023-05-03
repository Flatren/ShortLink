import { createApp } from 'vue'
import App from './App.vue'
import Er404 from './components/Er404.vue'
import Main from './components/Main.vue'
import axios from 'axios'
import {createRouter, createWebHistory} from "vue-router"
function To(to)
{
        if (to.params.hash == "404" || to.params.hash == "next")
        {
            return "/"+to.params.hash
        }
        try {
            axios({
            method: "POST",
            url: '/api/get_link',
            data:{hash: to.params.hash},
            }).then(response=>{
                console.log(JSON.stringify(response))
                let url = "";
                let error = "";
                url = response.data.response;
                error = response.data.ERROR;
                if (url)
                    document.location.href=url;
                else
                    document.location.href = window.location.origin+"/404";
            })
        } catch (error_) {
            alert("Проблемы на сервере.");
        }
        
}
const router = createRouter(
    {
        history: createWebHistory(),
        routes:[
            {
                path: "/",
                component: Main,
            },
            {
                path: "/404",
                component: Er404,
            },
            {
                path: '/:hash',
                redirect:to => {To(to)}
            }
        ]
    }
)

import './assets/main.css'
createApp(App).use(router).mount('#app')
