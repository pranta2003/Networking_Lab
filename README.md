<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Networking_Lab - Git Author Correction Demo</title>
<style>
  body { font-family: Arial, sans-serif; background: #f0f0f0; margin: 0; padding: 20px; }
  h1, h2 { text-align: center; color: #333; }
  section { background: #fff; padding: 20px; border-radius: 10px; margin: 20px auto; max-width: 800px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); }
  pre { background: #1e1e1e; color: #00ff00; padding: 15px; border-radius: 8px; overflow-x: auto; font-family: monospace; }
  .terminal { background: #1e1e1e; color: #00ff00; padding: 20px; border-radius: 10px; font-family: monospace; margin-top: 20px; white-space: pre-wrap; }
  .line { opacity: 0; margin: 2px 0; transition: opacity 0.5s; }
  button { display: block; margin: 20px auto; padding: 10px 20px; font-size: 16px; border-radius: 5px; cursor: pointer; }
</style>
</head>
<body>

<h1>Networking_Lab - Git Author Correction Demo</h1>

<section>
<h2>Instructions</h2>
<p>This demo shows how to correct the <strong>author name and email</strong> in your Git repository history.</p>

<h3>Steps</h3>
<ol>
<li>Open your terminal (PowerShell, Git Bash, or Linux/Mac Terminal).</li>
<li>Navigate to your repository folder:</li>
<pre>cd /path/to/your/repo</pre>
<li>Run the command to rewrite commit history:</li>
<pre id="commands">git filter-branch --env-filter "
CORRECT_NAME=\"Pranta Kumer Pandit\"
CORRECT_EMAIL=\"prantakumerpandit@gmail.com\"

export GIT_COMMITTER_NAME=\"$CORRECT_NAME\"
export GIT_COMMITTER_EMAIL=\"$CORRECT_EMAIL\"
export GIT_AUTHOR_NAME=\"$CORRECT_NAME\"
export GIT_AUTHOR_EMAIL=\"$CORRECT_EMAIL\"
" -- --all</pre>
<li>Force push the changes to GitHub:</li>
<pre id="push">git push origin --force --all
git push origin --force --tags</pre>

<button onclick="copyAll()">Copy All Commands</button>
</ol>
</section>

<section>
<h2>Live Terminal Animation</h2>
<div class="terminal" id="terminal">
  <div class="line">cd Networking_Lab</div>
  <div class="line">git filter-branch --env-filter &quot;CORRECT_NAME=&quot;Pranta Kumer Pandit&quot;&quot;</div>
  <div class="line">CORRECT_EMAIL=&quot;prantakumerpandit@gmail.com&quot;</div>
  <div class="line">export GIT_COMMITTER_NAME=&quot;$CORRECT_NAME&quot;</div>
  <div class="line">export GIT_COMMITTER_EMAIL=&quot;$CORRECT_EMAIL&quot;</div>
  <div class="line">export GIT_AUTHOR_NAME=&quot;$CORRECT_NAME&quot;</div>
  <div class="line">export GIT_AUTHOR_EMAIL=&quot;$CORRECT_EMAIL&quot;</div>
  <div class="line">-- --all</div>
  <div class="line">git push origin --force --all</div>
  <div class="line">git push origin --force --tags</div>
</div>
</section>

<script>
const lines = document.querySelectorAll('.line');
let i = 0;
function showLine() {
  if(i < lines.length) {
    lines[i].style.opacity = 1;
    i++;
    setTimeout(showLine, 800); // speed per line
  }
}
showLine();

// Copy all commands button
function copyAll() {
  const text = document.getElementById('commands').innerText + '\n' + document.getElementById('push').innerText;
  navigator.clipboard.writeText(text).then(() => {
    alert('All Git commands copied to clipboard!');
  });
}
</script>

</body>
</html>
