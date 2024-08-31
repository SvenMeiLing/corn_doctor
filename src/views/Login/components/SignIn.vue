<template>
    <n-card class="w-full">
        <n-form
                ref="formRef"
                :model="formValue"
                :rules="rules"
                :validate-messages="messages"
        >
            <n-form-item label="密钥" path="secretKey">
                <n-input v-model:value="formValue.secretKey" placeholder="Input Secret Key" type="password"/>
            </n-form-item>
            <n-form-item>
                <n-button @click="handleValidateClick">
                    验证
                </n-button>
            </n-form-item>
        </n-form>
        <pre>{{ JSON.stringify(formValue, null, 2) }}</pre>
    </n-card>
</template>

<script setup>
import {ref} from 'vue'
import {useRouter} from 'vue-router'
import {useUserProfile} from "@/stores/userProfile.js";

const userProfile = useUserProfile()
const router = useRouter()

const formRef = ref(null);
const formValue = ref({
    secretKey: "corn-doctor"
})
const messages = {
    required: "%s 是必须的"
}
const rules = {
    user: {
        name: {
            required: true,
            trigger: "blur"
        }
    }
}
const handleValidateClick = (e) => {
    e.preventDefault();
    // req to api
    formRef.value?.validate(async (errors) => {
        if (!errors) {
            await userProfile.getAccessToken()
            await router.push("/")
            window.$message.success("好");
        } else {
            console.log(errors);
            window.$message.error("不好");
        }
    });
}
</script>

<style scoped>

</style>
