import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Login from '@/views/Login'
import Home from '@/views/Home'
import secm from '@/views/operation/secm/secmanager'
import userinfo from '@/views/userinformation/userinfo'
import employee from '@/views/operation/emp/employee'
import sysmonitor from '@/views/operation/sysmonitor/systemmonitor'
import itemManager from '@/views/schedule/itemManager/manager'
import schedulemanager from '@/views/schedule/scheduleManager/scheduleInfo'
import participantsinfo from '@/views/schedule/participantsinfo/participantsinfo'
import Test from '@/views/test'


import BridgeSynthesis from '@/views/structure/branch/BridgeSynthesis'
import HealthMonitor from '@/views/structure/branch/HealthMonitor'
import NavigationBridge from '@/views/structure/branch/NavigationBridge'
import NonNavigationBridge from '@/views/structure/branch/NonNavigationBridge'
import ProtectiveScreen from '@/views/structure/branch/ProtectiveScreen'
import BridgeLightAndElectric from '@/views/structure/branch/BridgeLightAndElectric'
import WholeModel from '@/views/structure/branch/WholeModel'
import Log from '@/views/structure/branch/Logs'
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
          path:'/2-1',
          name: '2-1',
          component: WholeModel
        },
        {
          path:'/2-2',
          name: '2-2',
          component: NavigationBridge
        },
        {
          path:'/2-3',
          name: '2-3',
          component: NonNavigationBridge
        },
        {
          path:'/2-4',
          name: '2-4',
          component: ProtectiveScreen
        },
        {
          path:'/2-5',
          name: '2-5',
          component: BridgeSynthesis
        },
        {
          path:'/2-6',
          name: '2-6',
          component: BridgeLightAndElectric
        },
        {
          path: '/2-7',
          name: '2-7',
          component: HealthMonitor
        },
        {
          path: '/2-8',
          name: '2-8',
          component: Log
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
