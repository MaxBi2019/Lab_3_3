""""Mover module"""
import shutil


def bring(name):
    """
    :param name: str()
    :return:
    ------------------
    Rewrite file and fatch it to apropriate directory
    """
    with open(name + ".html", 'r+', encoding="utf-8", errors="ignore") as file:
        lst = file.readlines()
        file.seek(0)
        lst.insert(3, """
        <style>
        .a{
            color: #5175ed;
            font-size: medium;
            font-family: 'Consolas', 'Deja Vu Sans Mono', 'Bitstream Vera Sans Mono', monospace;
        }
        </style>
        <a id="demo">Exit</a>
        <script>
        function getURL() {
            return location.href}
        var n = getURL().toString();
        var s = n.length;
        var s = n.slice(0, s-3);
        document.getElementById("demo").setAttribute("href", s);
        </script>""")
        for elm in lst:
            file.write(elm)
    shutil.move(f'{name}.html', f'templates/{name}.html')
