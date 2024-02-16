def generate_git_script(id):
    return f"""
if [ ! -d {id} ]; then
    git clone https://github.com/{id}/project {id}
else
    (cd {id}; git pull)
fi
""".strip()

# print(generate_git_script("3333333333333"))