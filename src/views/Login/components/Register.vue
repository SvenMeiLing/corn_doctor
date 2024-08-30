<template>
    <n-card class="w-full box-border">
        <n-form ref="formRef" :model="modelRef" :rules="rules">
            <n-form-item path="username" label="用户名">
                <n-input v-model:value="modelRef.username" @keydown.enter.prevent/>
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
                                :disabled="modelRef.username === null"
                                round
                                type="primary"
                                @click="handleValidateButtonClick"
                        >
                            提交
                        </n-button>
                    </div>
                </n-col>
            </n-row>
        </n-form>
    </n-card>
</template>

<script setup>
import {ref} from 'vue'
import {useMessage} from 'naive-ui'

const formRef = ref(null);
const rPasswordFormItemRef = ref(null);
const message = useMessage();
const modelRef = ref({
    username: null,
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
    username: [
        {
            required: true,
            validator(rule, value) {
                if (!value) {
                    return new Error("需要输入账户");
                } else if (value.length < 6) {
                    return new Error("用户名不可小于6位字符");
                } else if (value.length > 10) {
                    return new Error("用户名不可大于10位字符");
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

</style>
