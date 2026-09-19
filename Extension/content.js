console.log("Phishing Guard content script injected");

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    sendResponse({ received: true });

    if (!message || message.type !== "PHISHING_DETECTED") {
        return true;
    }

    const currentUrl = location.href;

    console.log("Content.js nhận message:", message);
    console.log("Current tab URL:", currentUrl);

    const warningPage =
        chrome.runtime.getURL("warning.html") +
        "?url=" + encodeURIComponent(currentUrl);

    console.log("Redirect to warning:", warningPage);

    window.stop();
    window.location.replace(warningPage);

    return true; 
});
