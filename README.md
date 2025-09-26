<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Networking_Lab - Git Author Correction Demo</title>
<style>
  body { font-family: Arial, sans-serif; background: #f0f0f0; margin: 0; padding: 20px; }
  h1 { text-align: center; color: #333; }
  section { background: #fff; padding: 20px; border-radius: 10px; margin: 20px auto; max-width: 800px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); }
  h2 { color: #444; }
  pre { background: #1e1e1e; color: #00ff00; padding: 15px; border-radius: 8px; overflow-x: auto; font-family: monospace; }
  .terminal { background: #1e1e1e; color: #00ff00; padding: 20px; border-radius: 10px; text-align: left; font-family: monospace; margin-top: 20px; }
  .line { opacity: 0; margin: 2px 0; }
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
<pre>git filter-branch --env-filter '
CORRECT_NAME="Pranta Kumer Pandit"
CORRECT_EMAIL="prantakumerpandit@gmail.com"

export GIT_COMMITTER_NAME="$CORRECT_NAME"
export GIT_COMMITTER_EMAIL="$CORRECT_EMAIL"
export GIT_AUTHOR_NAME="$CORRECT_NAME"
export GIT_AUTHOR_EMAIL="$CORRECT_EMAIL"
' -- --all</pre>
<li>Force push the changes to GitHub:</li>
<pre>git push origin --force --all
git push origin --force --tags</pre>
</ol>
</section>

<section>
<h2>Live Terminal Animation</h2>
<div class="terminal" id="terminal">
  <div class="line">cd Networking_Lab</div>
  <div class="line">git filter-branch --env-filter '</div>
  <div class="line">CORRECT_NAME="Pranta Kumer Pandit"</div>
  <div class="line">CORRECT_EMAIL="prantakumerpandit@gmail.com"</div>
  <div class="line">export GIT_COMMITTER_NAME="$CORRECT_NAME"</div>
  <div class="line">export GIT_COMMITTER_EMAIL="$CORRECT_EMAIL"</div>
  <div class="line">export GIT_AUTHOR_NAME="$CORRECT_NAME"</div>
  <div class="line">export GIT_AUTHOR_EMAIL="$CORRECT_EMAIL"</div>
  <div class="line">' -- --all</div>
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
    setTimeout(showLine, 1000); // delay per line
  }
}
showLine();
</script>

</body>
</html>
