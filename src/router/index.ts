import { createRouter, createWebHashHistory, RouteRecordRaw } from "vue-router";
import Cloud from "../views/Cloud.vue";
import MakeBot from "../views/Make.vue";
import Home from "../views/Home.vue";
import Premade from "../views/Premade.vue";
import Edit from "../views/Edit.vue";
import Find from "../views/Find.vue";
const routes: Array<RouteRecordRaw> = [
  {
    path: "/make-bot",
    name: "MakeBot",
    component: MakeBot,
  },
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/upload",
    name: "Upload",
    component: Cloud,
  },
  {
    path: "/interface/:uuid",
    name: "Premade",
    component: Premade,
  },
  {
    path: "/edit",
    name: "Edit",
    component: Edit,
  },
  {
    path: "/find",
    name: "Find",
    component: Find,
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
