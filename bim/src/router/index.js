import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Login from '@/views/Login'
import Home from '@/views/Home'
// import Page1 from '@/views/Page1'
import secm from '@/views/operation/secm/secmanager'
import userinfo from '@/views/userinformation/userinfo'
import employee from '@/views/operation/emp/employee'
import sysmonitor from '@/views/operation/sysmonitor/systemmonitor'
import itemManager from '@/views/schedule/itemManager/manager'
import schedulemanager from '@/views/schedule/scheduleManager/scheduleInfo'
import participantsinfo from '@/views/schedule/participantsinfo/participantsinfo'
import Test from '@/views/test'
import bridgesynthesisinfo from '@/views/structure/branch/bridgesynthesisInfo'
import health from '@/views/structure/branch/health'


Vue.use(Router)

export default new Router({
  mode: "history",
  routes: [
    {
      path: '/',
      name: 'Login',
      component: Login
    },
    {
      path: '/home',
      name: 'Home',
      component: Home,
      children: [
        {
          path:'/2-5',
          name: '2-5',
          component: bridgesynthesisinfo
        },
        {
          path: '/4-1',
          name: '4-1',
          component: itemManager
        },
        {
          path: '/4-2',
          name: '4-2',
          component: schedulemanager
        },
        {
          path: '/4-3',
          name: '4-3',
          component: participantsinfo
        },
        {
            path: '/5-1',
            name: '5-1',
            component: employee,
        },
        {
            path: '/5-2',
            name: '5-2',
            component: secm,
        },
        {
            path: '/5-3',
            name: '5-3',
            component: sysmonitor,
        },
        {
            path: '/6',
            name: '6',
            component: userinfo,
        },
        {
          path: '/test',
          name: 'test',
          component: Test
        },
        {
          path: '/health',
          name: 'health',
          component: health
        },
        
      ],
    },


    
    // {
    //   path: "/404",
    //   name: "notFound",
    //   component: notFound
    // }, 



    // {
    //   path: "*", // 此处需特别注意置于最底部
    //   redirect: "/404"
    // }


  ]
})
