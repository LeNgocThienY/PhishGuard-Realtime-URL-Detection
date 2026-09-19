document.addEventListener("DOMContentLoaded", () => {
    const params = new URLSearchParams(location.search);
    const urlParam = params.get("url");
    const badUrlEl = document.getElementById("badUrl");

    // Nút quay lại
    const backBtn = document.getElementById("backBtn");
    if (backBtn) {
        backBtn.addEventListener("click", (e) => {
            e.preventDefault();

            if (history.length > 1) {
                history.back();
            } else {
                window.close();
            }
        });
    }

    // Nút tiếp tục truy cập
    const continueBtn = document.getElementById("continueBtn");
    if (continueBtn) {
        continueBtn.addEventListener("click", (e) => {
            e.preventDefault();
            if (!urlParam) return;

            let originalUrl = decodeURIComponent(urlParam);

            try {
                const urlObj = new URL(originalUrl);
                // Thêm param bypass để background không chặn lại lần nữa
                urlObj.searchParams.set("__phish_bypass", "1");
                const bypassUrl = urlObj.toString();

                window.location.href = bypassUrl;
            } catch (err) {
                console.error("Không parse được URL, fallback:", err);
                // Nếu parse lỗi, cứ truy cập thẳng (có thể bị chặn lại)
                window.location.href = originalUrl;
            }
        });
    }
});
