<template>
    <div class="w-full h-full bg-img">
        <div class="flex h-full items-center justify-center">
            <div class="rounded bg-white/60 dark:bg-black/90 h-82 w-1/2 box-border p-5">
                <n-form ref="formRef" :model="modelRef" :rules="rules">
                    <n-form-item path="age" label="年龄">
                        <n-input v-model:value="modelRef.age" @keydown.enter.prevent/>
                    </n-form-item>
                    <n-form-item path="password" label="密码">
                        <n-input
                                v-model:value="modelRef.password"
                                type="password"
                                @input="handlePasswordInput"
                                @keydown.enter.prevent
                        />
                    </n-form-item>
                    <n-form-item
                            ref="rPasswordFormItemRef"
                            first
                            path="reenteredPassword"
                            label="重复密码"
                    >
                        <n-input
                                v-model:value="modelRef.reenteredPassword"
                                :disabled="!modelRef.password"
                                type="password"
                                @keydown.enter.prevent
                        />
                    </n-form-item>
                    <n-row :gutter="[0, 24]">
                        <n-col :span="24">
                            <div style="display: flex; justify-content: flex-end">
                                <n-button
                                        :disabled="modelRef.age === null"
                                        round
                                        type="primary"
                                        @click="handleValidateButtonClick"
                                >
                                    验证
                                </n-button>
                            </div>
                        </n-col>
                    </n-row>
                </n-form>

                <n-text tag="pre">{{ JSON.stringify(modelRef, null, 2) }}</n-text>
            </div>
        </div>
    </div>
</template>

<script setup>
import {ref} from 'vue'
import {useMessage} from 'naive-ui'

const formRef = ref(null);
const rPasswordFormItemRef = ref(null);
const message = useMessage();
const modelRef = ref({
    age: null,
    password: null,
    reenteredPassword: null
});

function validatePasswordStartWith(rule, value) {
    return !!modelRef.value.password && modelRef.value.password.startsWith(value) && modelRef.value.password.length >= value.length;
}

function validatePasswordSame(rule, value) {
    return value === modelRef.value.password;
}

const handlePasswordInput = () => {
    if (modelRef.value.reenteredPassword) {
        rPasswordFormItemRef.value?.validate({trigger: "password-input"});
    }
}

const handleValidateButtonClick = (e) => {
    e.preventDefault();
    formRef.value?.validate((errors) => {
        if (!errors) {
            message.success("验证成功");
        } else {
            console.log(errors);
            message.error("验证失败");
        }
    });
}
const rules = {
    age: [
        {
            required: true,
            validator(rule, value) {
                if (!value) {
                    return new Error("需要年龄");
                } else if (!/^\d*$/.test(value)) {
                    return new Error("年龄应该为整数");
                } else if (Number(value) < 18) {
                    return new Error("年龄应该超过十八岁");
                }
                return true;
            },
            trigger: ["input", "blur"]
        }
    ],
    password: [
        {
            required: true,
            message: "请输入密码"
        }
    ],
    reenteredPassword: [
        {
            required: true,
            message: "请再次输入密码",
            trigger: ["input", "blur"]
        },
        {
            validator: validatePasswordStartWith,
            message: "两次密码输入不一致",
            trigger: "input"
        },
        {
            validator: validatePasswordSame,
            message: "两次密码输入不一致",
            trigger: ["blur", "password-input"]
        }
    ]
};
</script>

<style scoped>
.bg-img {
    background-image: url("/src/assets/images/pexels-ironic-751096.jpg");
    background-repeat: no-repeat;
    background-size: 100% 100%;
}
</style>
