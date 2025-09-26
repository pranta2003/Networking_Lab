# Networking_Lab - Git Author Correction Demo

This repository demonstrates how to **correct Git commit author and email** in an existing repository using Git commands.  

It includes a **live HTML animation** showing the steps for beginners.  

---

## Steps to Correct Git Author

1. Open your terminal (PowerShell, Git Bash, or Linux/Mac Terminal).
2. Navigate to your repository folder:


cd /path/to/your/repo
Run the following command to rewrite history with your correct name/email:

git filter-branch --env-filter '
CORRECT_NAME="Your Full Name"
CORRECT_EMAIL="your.email@example.com"

export GIT_COMMITTER_NAME="$CORRECT_NAME"
export GIT_COMMITTER_EMAIL="$CORRECT_EMAIL"
export GIT_AUTHOR_NAME="$CORRECT_NAME"
export GIT_AUTHOR_EMAIL="$CORRECT_EMAIL"
' -- --all


Force push to GitHub:

git push origin --force --all
git push origin --force --tags

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Git Author Correction Animation</title>
<style>
  body { font-family: Arial, sans-serif; text-align: center; background: #f0f0f0; }
  .terminal { background: #1e1e1e; color: #00ff00; padding: 20px; border-radius: 10px; display: inline-block; margin-top: 50px; text-align: left; font-family: monospace; }
  .line { opacity: 0; }
</style>
</head>
<body>
<h1>Git Author Correction Animation</h1>
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

<script>
const lines = document.querySelectorAll('.line');
let i = 0;
function showLine() {
  if(i < lines.length) {
    lines[i].style.opacity = 1;
    i++;
    setTimeout(showLine, 1000); // 1 second delay per line
  }
}
showLine();
</script>
</body>
</html>
