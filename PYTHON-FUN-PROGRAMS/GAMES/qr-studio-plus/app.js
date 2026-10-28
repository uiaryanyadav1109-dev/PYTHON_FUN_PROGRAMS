const $=id=>document.getElementById(id);let type='url',content='',logo=null,toastTimer=null;
const templates={url:`<label for="mainInput">Website URL</label><input id="mainInput" type="url" placeholder="https://example.com"><div class="hint">Include https:// for best results.</div>`,text:`<label for="mainInput">Your text</label><textarea id="mainInput" placeholder="Type a message, address or any text..."></textarea>`,wifi:`<label for="ssid">Network name (SSID)</label><input id="ssid" placeholder="Your Wi-Fi name"><label for="wifiPass">Network password</label><input id="wifiPass" type="password" placeholder="Wi-Fi password"><label for="security">Security type</label><select id="security"><option value="WPA">WPA / WPA2 / WPA3</option><option value="WEP">WEP</option><option value="nopass">No password</option></select><div class="hint">Anyone who scans the code may be able to join this network.</div>`,email:`<label for="emailTo">Email address</label><input id="emailTo" type="email" placeholder="hello@example.com"><label for="subject">Subject (optional)</label><input id="subject" placeholder="Hello there"><label for="message">Message (optional)</label><textarea id="message" placeholder="Write a message..."></textarea>`,phone:`<label for="phoneNo">Phone number</label><input id="phoneNo" type="tel" placeholder="+91 98765 43210"><div class="hint">Include your country code for international numbers.</div>`,sms:`<label for="smsNo">Phone number</label><input id="smsNo" type="tel" placeholder="+91 98765 43210"><label for="smsMessage">SMS message (optional)</label><textarea id="smsMessage" placeholder="Type your message..."></textarea>`};
function toast(msg,error=false){$('toast').textContent=msg;$('toast').classList.toggle('error',error);$('toast').classList.add('show');clearTimeout(toastTimer);toastTimer=setTimeout(()=>$('toast').classList.remove('show'),2600)}
function setType(t){type=t;document.querySelectorAll('.type').forEach(b=>b.classList.toggle('active',b.dataset.type===t));$('fields').innerHTML=templates[t];hideQR()}
document.querySelectorAll('.type').forEach(b=>b.addEventListener('click',()=>setType(b.dataset.type)));
function wifiEscape(s){return s.replace(/([\\;,:"])/g,'\\$1')}
function getContent(){if(type==='url'){let v=$('mainInput').value.trim();if(!v)throw Error('Enter a website URL first.');let u;try{u=new URL(v)}catch{throw Error('Enter a valid URL, such as https://example.com.')}if(!['http:','https:'].includes(u.protocol))throw Error('Only HTTP and HTTPS links are supported.');return u.href}if(type==='text'){let v=$('mainInput').value.trim();if(!v)throw Error('Enter some text first.');return v}if(type==='wifi'){let s=$('ssid').value,p=$('wifiPass').value,sec=$('security').value;if(!s.trim())throw Error('Enter your Wi-Fi network name.');if(sec!=='nopass'&&!p)throw Error('Enter your Wi-Fi password.');return `WIFI:T:${sec};S:${wifiEscape(s)};P:${sec==='nopass'?'':wifiEscape(p)};;`}if(type==='email'){let e=$('emailTo').value.trim();if(!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(e))throw Error('Enter a valid email address.');return `mailto:${e}?subject=${encodeURIComponent($('subject').value)}&body=${encodeURIComponent($('message').value)}`}if(type==='phone'||type==='sms'){let p=$('phoneNo').value.trim();if(!/^\+?[0-9\s().-]{7,20}$/.test(p))throw Error('Enter a valid phone number.');p=p.replace(/[\s().-]/g,'');return type==='phone'?`tel:${p}`:`SMSTO:${p}:${$('smsMessage').value}`}}
function hideQR(){$('qrOutput').style.display='none';$('qrOutput').innerHTML='';$('empty').style.display='block';$('meta').style.display='none';$('downloads').style.display='none';content=''}
function generate(){if(typeof QRCode==='undefined')return toast('QR library failed to load. Check your internet connection.',true);try{content=getContent();if($('dark').value.toLowerCase()===$('light').value.toLowerCase())throw Error('Choose different foreground and background colors.');const size=+$('size').value,margin=+$('margin').value,dark=$('dark').value,light=$('light').value,level=$('level').value;const holder=document.createElement('div');new QRCode(holder,{text:content,width:size,height:size,colorDark:dark,colorLight:light,correctLevel:QRCode.CorrectLevel[level]});setTimeout(()=>{const src=holder.querySelector('canvas');if(!src)return toast('Could not render the QR code. Try shorter content.',true);const pad=margin,caption=$('labelText').checked,frame=$('frame').checked,top=frame?36:pad,bottom=pad+(caption?42:0),out=document.createElement('canvas');out.width=size+pad*2;out.height=size+top+bottom;const ctx=out.getContext('2d');ctx.fillStyle=light;ctx.fillRect(0,0,out.width,out.height);ctx.drawImage(src,pad,top,size,size);const finish=()=>{if(logo){const max=size*.19;let w=logo.width,h=logo.height,scale=Math.min(max/w,max/h);w*=scale;h*=scale;const x=(out.width-w)/2,y=top+(size-h)/2;ctx.fillStyle=light;ctx.beginPath();ctx.roundRect(x-7,y-7,w+14,h+14,9);ctx.fill();ctx.drawImage(logo,x,y,w,h)}if(frame){ctx.fillStyle=dark;ctx.font='700 13px system-ui';ctx.textAlign='center';ctx.fillText('SCAN ME',out.width/2,23)}if(caption){ctx.fillStyle=dark;ctx.font='600 11px system-ui';ctx.textAlign='center';ctx.fillText(type==='url'?'SCAN TO OPEN':type==='wifi'?'SCAN TO CONNECT':type==='email'?'SCAN TO EMAIL':type==='phone'?'SCAN TO CALL':type==='sms'?'SCAN TO MESSAGE':'SCAN TO READ',out.width/2,out.height-15)}$('qrOutput').innerHTML='';out.style.width='100%';out.style.height='auto';out.style.maxWidth='100%';$('qrOutput').appendChild(out);$('qrOutput').style.display='block';$('empty').style.display='none';$('meta').style.display='flex';$('downloads').style.display='grid';$('dimension').textContent=`${out.width} × ${out.height} px`;toast('Your QR code is ready!')};if(logo){if(logo.complete)finish();else logo.onload=finish}else finish()},40)}catch(e){toast(e.message||'Could not generate QR code.',true)}}
$('generate').addEventListener('click',generate);$('download').addEventListener('click',()=>{const c=$('qrOutput').querySelector('canvas');if(!c)return toast('Generate a QR code first.',true);const a=document.createElement('a');a.download='qr-nova.png';a.href=c.toDataURL('image/png');a.click();toast('PNG download started.')});$('copy').addEventListener('click',async()=>{if(!content)return toast('Generate a QR code first.',true);try{await navigator.clipboard.writeText(content);toast('Content copied!')}catch{toast('Clipboard access unavailable in this browser.',true)}});
$('reset').addEventListener('click',()=>{setType(type);$('size').value='260';$('level').value='M';$('margin').value='16';$('dark').value='#10213a';$('light').value='#ffffff';$('frame').checked=true;$('labelText').checked=true;logo=null;$('logoFile').value='';$('logoName').textContent='Optional';colorLabels();toast('Options reset.')});function colorLabels(){$('darkHex').textContent=$('dark').value.toUpperCase();$('lightHex').textContent=$('light').value.toUpperCase()}$('dark').addEventListener('input',colorLabels);$('light').addEventListener('input',colorLabels);document.querySelectorAll('.swatch').forEach(b=>b.addEventListener('click',()=>{$('dark').value=b.dataset.dark;$('light').value=b.dataset.light;colorLabels()}));$('logoFile').addEventListener('change',e=>{const f=e.target.files[0];if(!f){logo=null;$('logoName').textContent='Optional';return}if(f.size>2*1024*1024){e.target.value='';return toast('Choose a logo smaller than 2 MB.',true)}const reader=new FileReader();reader.onload=()=>{const img=new Image();img.onload=()=>{logo=img;$('logoName').textContent=f.name.length>18?f.name.slice(0,15)+'…':f.name;toast('Logo added. Generate again to apply it.')};img.src=reader.result};reader.readAsDataURL(f)});$('theme').addEventListener('click',()=>{document.body.classList.toggle('light');$('theme').textContent=document.body.classList.contains('light')?'☾ Theme':'☼ Theme'});$('fields').addEventListener('keydown',e=>{if(e.key==='Enter'&&e.target.tagName==='INPUT'&&!['subject'].includes(e.target.id)){e.preventDefault();generate()}});

// QR scanner: starts only after an explicit user action.
let qrScanner = null;
let scannerRunning = false;
const safeGet = id => document.getElementById(id);

function setScanStatus(message, error = false) {
  const el = safeGet('scanStatus');
  if (!el) return;
  el.textContent = message;
  el.style.color = error ? '#d9534f' : '';
}

function showScanResult(decodedText) {
  const result = safeGet('scanResult');
  const textEl = safeGet('scanText');
  const openBtn = safeGet('openScan');
  if (!result || !textEl || !openBtn) return;
  // Use textContent, never HTML, because QR content is untrusted input.
  textEl.textContent = String(decodedText).slice(0, 10000);
  result.hidden = false;
  openBtn.hidden = true;
  openBtn.dataset.url = '';
  try {
    const url = new URL(String(decodedText).trim());
    if ((url.protocol === 'https:' || url.protocol === 'http:') && url.hostname) {
      openBtn.hidden = false;
      openBtn.dataset.url = url.href;
    }
  } catch (_) {
    // QR content is not a valid web URL; display it as plain text.
  }
}

async function stopQrCamera(showMessage = true) {
  if (qrScanner) {
    try {
      if (scannerRunning) await qrScanner.stop();
    } catch (_) {
      // Ignore camera stop errors; reset the UI regardless.
    }
    try { await qrScanner.clear(); } catch (_) {}
  }
  scannerRunning = false;
  safeGet('stopCamera').disabled = true;
  safeGet('startCamera').disabled = false;
  if (showMessage) setScanStatus('Camera is off.');
}

async function startQrCamera() {
  if (typeof Html5Qrcode === 'undefined') {
    setScanStatus('Scanner library did not load. Check your internet connection and refresh.', true);
    return;
  }
  await stopQrCamera(false);
  safeGet('scanResult').hidden = true;
  safeGet('startCamera').disabled = true;
  setScanStatus('Requesting camera permission…');
  try {
    qrScanner = new Html5Qrcode('reader', { verbose: false });
    await qrScanner.start(
      { facingMode: 'environment' },
      { fps: 10, qrbox: { width: 240, height: 240 }, aspectRatio: 1.0 },
      async decodedText => {
        showScanResult(decodedText);
        setScanStatus('QR code scanned successfully. Camera stopped.');
        await stopQrCamera(false);
        setScanStatus('QR code scanned successfully. Camera is off.');
      },
      () => { /* No QR found in this frame; keep scanning. */ }
    );
    scannerRunning = true;
    safeGet('stopCamera').disabled = false;
    safeGet('startCamera').disabled = true;
    setScanStatus('Camera is active. Point it at a QR code.');
  } catch (error) {
    scannerRunning = false;
    safeGet('startCamera').disabled = false;
    safeGet('stopCamera').disabled = true;
    const msg = error && error.name === 'NotAllowedError'
      ? 'Camera permission was denied. Allow camera access in your browser settings and try again.'
      : 'Could not start the camera. Use HTTPS, allow camera access, or scan an image instead.';
    setScanStatus(msg, true);
    try { if (qrScanner) await qrScanner.clear(); } catch (_) {}
  }
}

safeGet('createTab').addEventListener('click', async () => {
  await stopQrCamera(false);
  safeGet('createTab').classList.add('active');
  safeGet('scanTab').classList.remove('active');
  safeGet('createTab').setAttribute('aria-selected', 'true');
  safeGet('scanTab').setAttribute('aria-selected', 'false');
  safeGet('scannerPanel').hidden = true;
  document.querySelector('.layout').hidden = false;
});
safeGet('scanTab').addEventListener('click', () => {
  safeGet('scanTab').classList.add('active');
  safeGet('createTab').classList.remove('active');
  safeGet('scanTab').setAttribute('aria-selected', 'true');
  safeGet('createTab').setAttribute('aria-selected', 'false');
  document.querySelector('.layout').hidden = true;
  safeGet('scannerPanel').hidden = false;
});
safeGet('startCamera').addEventListener('click', startQrCamera);
safeGet('stopCamera').addEventListener('click', () => stopQrCamera());
safeGet('scanFile').addEventListener('change', async event => {
  const file = event.target.files && event.target.files[0];
  if (!file) return;
  const allowedTypes = ['image/png', 'image/jpeg', 'image/webp', 'image/gif'];
  if (!allowedTypes.includes(file.type) || file.size > 10 * 1024 * 1024) {
    setScanStatus('Choose a PNG, JPEG, WEBP or GIF image smaller than 10 MB.', true);
    event.target.value = '';
    return;
  }
  if (typeof Html5Qrcode === 'undefined') {
    setScanStatus('Scanner library did not load. Check your internet connection and refresh.', true);
    return;
  }
  await stopQrCamera(false);
  setScanStatus('Scanning image…');
  try {
    const scanner = new Html5Qrcode('reader', { verbose: false });
    const decodedText = await scanner.scanFile(file, true);
    showScanResult(decodedText);
    setScanStatus('QR code found in image.');
  } catch (_) {
    setScanStatus('No readable QR code found in this image. Try a clearer image with the full QR code visible.', true);
  } finally {
    try { if (qrScanner) await qrScanner.clear(); } catch (_) {}
    qrScanner = null;
    event.target.value = '';
  }
});
safeGet('copyScan').addEventListener('click', async () => {
  const value = safeGet('scanText').textContent || '';
  if (!value) return;
  try {
    await navigator.clipboard.writeText(value);
    setScanStatus('QR result copied to clipboard.');
  } catch (_) {
    setScanStatus('Clipboard access is unavailable. Select and copy the result manually.', true);
  }
});
safeGet('openScan').addEventListener('click', () => {
  const raw = safeGet('openScan').dataset.url;
  try {
    const url = new URL(raw);
    if (url.protocol !== 'https:' && url.protocol !== 'http:') return;
    // User must explicitly click. Open in a new tab without opener access.
    const opened = window.open(url.href, '_blank', 'noopener,noreferrer');
    if (!opened) setScanStatus('Your browser blocked the new tab. Copy the URL and open it manually.', true);
  } catch (_) {
    setScanStatus('This QR code does not contain a valid web link.', true);
  }
});
window.addEventListener('pagehide', () => {
  if (qrScanner && scannerRunning) qrScanner.stop().catch(() => {});
});
