console.log("Phishing URL Guard - Background chạy");
chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
    if (changeInfo.status !== "loading" || !tab.url || !tab.url.startsWith("http")) {
        return;
    }

    if (tab.url.includes("__phish_bypass=1")) {
        console.log("Bypass phishing check cho URL:", tab.url);
        return;
    }

    let cleanUrl = tab.url;

    console.log("Đang kiểm tra URL:", cleanUrl);

    fetch("http://127.0.0.1:5000/phish-url-prediction", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ url: cleanUrl })
    })
        .then(r => r.json())
        .then(data => {
            console.log("Kết quả từ AI:", data);

            if (data.label === 1) {  
                chrome.tabs.sendMessage(
                    tabId,
                    {
                        type: "PHISHING_DETECTED",
                        url: cleanUrl
                    },
                    () => {
                        if (chrome.runtime.lastError) {
                            console.warn("Không gửi được message:", chrome.runtime.lastError.message);
                        }
                    }
                );
            }
        })
        .catch(err => {
            console.error("Lỗi khi gọi API phishing:", err);
        });
});
