/* 
    *global console
    *FileName:menu_layout.js
    *PATH:static/js
    *Time: 2023/5/30 22:08
    *Author: zzy
*/


const fetchUserEmail = async () => {
    let email = "";
    await axios.get(
        "/user/get_email"
    ).then((response) => {
        let data = response.data
        if (data) {
            email = data
        } else {
            email = "访客"
        }
    }).catch((error) => {
        console.log(error)
        Swal.fire(
            {
                title: '网络似乎有问题?',
                text: '请检查您的网络状态是否正常?',
                icon: 'question',
                showConfirmButton: true,
                showCancelButton: true,
                confirmButtonText: '刷新',
                cancelButtonText: '取消'
            }
        ).then((result) => {
            if (result.isConfirmed) {
                // 选择确认框, 刷新当前页
                window.location.reload()
            }
        })
    })
    return email
}

function downloadFile(url) {
    // 下载文件
    fetch(url)
        .then(response => response.blob())
        .then(blob => {
            const url = window.URL.createObjectURL(blob);
            const anchorElement = document.createElement('a');
            anchorElement.href = url;
            anchorElement.download = 'result.mp4'; // 设置下载的文件名
            anchorElement.click();
            window.URL.revokeObjectURL(url);
        })
        .catch(error => {
            console.error('文件下载失败:', error);
        });
}

$(function () {
    const menuLinks = document.querySelectorAll('[href^="#menu"]');
    let charts1;
    let charts2;
    menuLinks.forEach((menuLink) => {
        // 遍历每个a标签
        menuLink.addEventListener('click', (event) => {
            $(".btn-close").click()  // 关闭offcanvas框
            event.preventDefault();
            const targetId = menuLink.getAttribute('href').substring(1);
            if (targetId === "menu3") {
                // 对移动设备的处理
                mobileHandler()
            } else if (targetId === "menu6") {
                // 请求省份列表
                getProvincesList()
            } else if (targetId === "menu7") {
                // 请求图表所需数据并绘制
                collectReqData().then(r => {
                    charts1 = r[1];  // 图表对象
                    const maxValueItem = r[0].reduce((prev, current) => prev.value > current.value ? prev : current);
                    let diseaseName = maxValueItem.name
                    $("#disease-name").text(diseaseName)
                })
                // 绘制第二种图表
                collectReqData2().then(r => {
                    charts2 = r; // 图表对象
                })
                window.addEventListener("resize", function () {
                    charts1.resize();
                    charts2.resize();
                    console.log('resize...')
                });
                console.log("echarts 绘制完成")
            } else if (targetId === "menu5") {
                let email;
                fetchUserEmail().then((r) => {
                    email = r
                    $(".fillEmail").text(email)
                })
                $("#spinner").addClass("animate__fadeIn") // 加载动画
            }
            const targetContent = document.getElementById(targetId);
            const allContents = document.getElementsByClassName('content');
            for (let i = 0; i < allContents.length; i++) {
                allContents[i].style.display = 'none';
            }
            targetContent.style.display = 'block';
        });
    });
    mobileHandler()

    // 焦点定位到当前页对应标签按钮上
    $(document).ready(function () {
        $('nav a').on("click", function () {
            $('a').removeClass('active');
            $(this).addClass('active');
        });
    });
    //操作表单的逻辑
    $(document).ready(function () {
        // 监听表单的submit事件
        document.querySelector('#myForm').addEventListener('submit', function (event) {
            // 阻止表单的默认提交行为
            event.preventDefault();
            // 在此处编写其他代码，例如使用AJAX异步提交表单数据等
        });
        //input输入框一定要加上name="file" flask才能接收到文件
        $("#submitBtn").on("click", function () {
            // 检查表单完整性
            const file = $("#fileInput")[0].files[0]
            if (!file) {
                console.log('没有图片')
                $("#closeMenu2Modal").click()
                let errorText = $("#error-warning-text")
                errorText.text("您还未选择文件, 请至少选择一个文件!")
                errorText.parent().removeClass("d-none")  // 隐藏alert
                setTimeout(function () {
                    errorText.parent().addClass("d-none")
                }, 2500)
                return false
            } else {
                let tagForm = $("#myForm")[0]
                let formData = new FormData(tagForm);

                // 点击提交按钮后显示加载动画
                $('#menu2Loading').html(
                    `<div class="spinner-grow text-success" role="status">
                    <span class="visually-hidden">Loading...</span>
                </div>`
                )
                $.ajax({
                    url: $(tagForm).attr("action"),
                    type: "POST",
                    data: formData,  // 请求数据为表单数据
                    cache: false,
                    contentType: false,
                    processData: false,
                    success: function (response) {
                        // 关闭模态对话框
                        $("#closeMenu2Modal").click()
                        // 置空tbody
                        $("tbody").html("")
                        // 加载response
                        let lst = response.result;
                        let index = 0;
                        let imgFileList = $("#fileInput").prop("files")
                        console.log(imgFileList)
                        for (let obj of lst) {
                            // 遍历每个对象的name, description属性
                            $("#tbody").append(
                                `<tr>
                                <th scope="row">
                                    <img src="${URL.createObjectURL(imgFileList[index])}"
                                        alt="uploaded image" style="width: 100%; height:auto;border-radius:7px 7px 7px 7px">
                                </th>
                                <td>${obj.name}</td>
                                <td>${obj.time_consume}<b>/</b>${(obj.recognition_rate * 100).toFixed(2) + '%'}</td>
                                <td>${obj.description}</td>
                            </tr>`
                            )
                            index++
                        }
                        $("#menu2Loading").toggle(400)
                        console.log(response.time)

                    },
                    error: function (xhr) {
                        // 处理错误响应, 上传文件
                        // 显示错误提示框
                        console.log(xhr.status)
                        $("#closeMenu2Modal").click()  // 关闭模态对话框

                        let alertBox = $('#error-alert');

                        if (xhr.status === 404) {
                            alertBox.text(`status:${xhr.status}-请检查您的网络配置!`);  // 设置错误信息文本
                        } else if (xhr.status >= 500) {
                            alertBox.text(`status:${xhr.status}-服务器正在维护中, 请稍后再试!`)
                        } else {
                            alertBox.text(`status:${xhr.status}-未知错误!`)
                        }

                        alertBox.removeClass('d-none');  // 移除默认隐藏样式
                        $("#menu2Loading").empty();
                        // 3秒后关闭错误提示框
                        let timerId = setTimeout(function () {
                            alertBox.addClass("d-none");
                        }, 3000);
                        // 点击提示框时立即关闭，并清除定时器
                        alertBox.click(() => {
                            clearTimeout(timerId);
                            alertBox.addClass("d-none");
                        });
                        $("#menu2Loading").toggle(400)
                    }
                });
                return false;
            }

        });
    });

    // 绑定登出事件
    $("#logout").on('click', function (event) {
        Swal.fire({
            title: '确认退出登录吗?',
            text: "账户注销后将要重新登陆",
            html: "倒计时:<b></b>ms后自动关闭",
            icon: 'warning',
            showConfirmButton: true,
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: '确认',
            cancelButtonText: '取消',
            timer: 2000,
            timerProgressBar: true,
            didOpen: () => {
                const b = Swal.getHtmlContainer().querySelector('b')
                timerInterval = setInterval(() => {
                    b.textContent = Swal.getTimerLeft()
                }, 100)
            },
            willClose: () => {
                clearInterval(timerInterval)
            }
        }).then((result) => {
            if (result.isConfirmed) {

                Swal.fire(
                    '成功退出登录!',
                    '你的身份信息已从本地清空!',
                    'success'
                )
                $.ajax({
                    url: "/user/logout",
                    method: "GET",
                    success: function (response) {
                        window.location.href = response.path;  // 注销成功回到首页
                    },
                    error: function (error) {
                        alert(error.error())
                        //清除所有cookie函数
                        window.location.href = '/';  // 注销成功回到首页
                    }
                })
            }
        })
    });
    // 侧边栏显示
    $("#rightMenuButton").on("click", function () {
        let email;
        fetchUserEmail().then((r) => {
            email = r
            $(".fillEmail").text(email)
        })
    })

    // 监听视频上传
    const videoForm = document.getElementById("videoForm"); // 获取表单元素
    const videoModal = $("#openModal")
    const submitBtn = $("#videoForm button[type=submit]")
    videoModal.on("click", () => {
        // 当再次开启模态对话框时
        // 置空文本提示信息
        $("#floatingTextarea").text("")
        // 重置表单
        $("#videoForm")[0].reset();
        // 清除进度条
        $("#progress-strip").html(
            `<div class="mb-3 progress" style="height: 0.15rem;"></div>`
        )
    })

    videoForm.addEventListener("submit", e => {
        e.preventDefault(); // 防止表单默认提交行为

        // 创建 FormData 对象存储表单数据
        const formData = new FormData(videoForm);
        let file = formData.get('videoFile')

        // 检查文件格式是否为 MP4
        if (file.type !== 'video/mp4') {
            // 如果文件格式不为 MP4，则做出相应的处理
            console.log(file.type)
            $("#floatingTextarea").text("您上传的格式非mp4类型哦!");
            return
        } else {
            $("#floatingTextarea").text("视频正在上传中, 等待时间约为两分钟...");
        }
        // 初始化进度条容器
        $("#progress-strip").html(
            `<div class="progress mb-3 animate__animated animate__zoomIn" role="progressbar" aria-label="Example 1px high"
                 aria-valuenow="25" aria-valuemin="0" aria-valuemax="100"
                 style="height: 0.15rem;">
                <div class="progress-bar" id="progress-bar" style="background-color: #e685b5;font-size: 0"></div>
            </div>`
        )
        // 创建一个随机数 90%-99%之间的随机数
        let targetProgress = Math.random() * 10 + 90
        // 设置初始进度
        let currentProgress = 0;
        // 每次增加的进度值，根据总时间(两分三十秒)和目标进度计算
        let increment = (targetProgress - currentProgress) / 2000;

        // 设置定时器, 每秒递增
        let interval = setInterval(function () {
            currentProgress += increment; // 每秒递增进度
            //显示到进度条上
            $('#progress-bar').css('width', currentProgress + '%').text(currentProgress.toFixed(2) + '%');

            if (currentProgress >= targetProgress) {
                // 如果当前进度达到随机数生成的阈值, 清除定时器
                clearInterval(interval);
            }
        }, 100); // 每秒递增进度

        // 禁用提交按钮
        submitBtn.prop('disabled', true);

        // 创建加载中的按钮
        let loadingButton = $('<button/>', {
            class: 'btn btn-primary',
            type: 'button',
            disabled: true,
        });
        let spinner = $('<span/>', {
            class: 'spinner-grow spinner-grow-sm',
            role: 'status',
            ariaHidden: true,
        });
        let buttonText = $('<span/>').text('处理中...');
        loadingButton.append(spinner).append(buttonText);

        // 将加载中的按钮替换为提交按钮
        submitBtn.replaceWith(loadingButton);

        // 发送 axios POST 请求，将表单数据提交到后端
        // 制作弹窗
        const Toast = Swal.mixin({
            toast: true,
            position: 'top-end',
            showConfirmButton: false,
            timer: 2750,
            timerProgressBar: true,
            didOpen: (toast) => {
                toast.addEventListener('mouseenter', Swal.stopTimer)
                toast.addEventListener('mouseleave', Swal.resumeTimer)
            }
        })
        // 提交视频到后端
        axios.post("/file/video", formData)
            .then(response => {
                // 请求成功
                console.log(response.data);
                clearInterval(interval); // 清除定时器
                // 进度条收尾
                $('#progress-bar').css('width', '100%');


                // 开启弹窗
                Toast.fire({
                    icon: 'success',
                    title: '成功处理, 可以点击下方提取下载到本地'
                })
                // 更改富文本框内容
                $("#floatingTextarea").text("视频处理完成, 四秒后自动为您关闭对话框")
                setTimeout(() => {
                    $(".btn-close").click() // 关闭模态对话框
                }, 4250)

                // 显示下载按钮
                $("#downloadLink").html(
                    `<a class="btn btn-lg animate__animated animate__fadeInBottomRight" style="background-color: #f1aeb5"
                                   onclick="downloadFile('/file/video_player')">
                        <img src="/static/images/receive.png" alt="" width="30">
                        提取结果
                    </a>`
                )
            })
            .catch(error => {
                // 请求失败
                console.error(error);
                // 提示错误弹窗
                Toast.fire({
                    icon: 'error',
                    title: '处理识别, 可能受网络影响或者视频内容不规范'
                })

            })
            .finally(() => {
                // 重置表单
                videoForm.reset();
                submitBtn.disabled = false; // 启用提交按钮
                // 恢复提交按钮
                loadingButton.replaceWith(submitBtn);
                submitBtn.prop('disabled', false);

            });

        submitBtn.disabled = true; // 禁用提交按钮，防止用户重复提交
    });
});

