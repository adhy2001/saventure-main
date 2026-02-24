import os
import re

def update_navbars(directory):
    new_nav_left = """            <!-- Logo (Left aligned for desktop and mobile) -->
            <a class="navbar-brand d-flex align-items-center gap-2 m-0" href="index.html">
                <!-- Desktop Logo -->
                <div class="logo-swap-container d-none d-lg-block">
                    <img src="images/Logo1.png" alt="Saventure Logo" class="logo-default" style="height: 38px;">
                    <img src="images/Logo name.png" alt="Saventure Name" class="logo-on-hover" style="height: 24px;">
                </div>
                <!-- Mobile Logo -->
                <div class="d-lg-none d-flex align-items-center gap-2">
                    <img src="images/Logo1.png" alt="Saventure Logo" class="nav-logo-mob" style="height: 30px; filter: brightness(0) invert(1);">
                    <img src="images/Logo name.png" alt="Saventure Name" class="nav-name-mob" style="height: 20px; filter: brightness(0) invert(1);">
                </div>
            </a>"""

    new_nav_links_open = """            <div class="collapse navbar-collapse justify-content-end" id="navbarNav">
                <ul class="navbar-nav mb-2 mb-lg-0 gap-lg-3 align-items-center">"""

    # Regex patterns to find sections
    # 1. Find mobile logo block to replace with new combined logo block
    mobile_logo_pattern = re.compile(
        r'<!-- Mobile Logo -->.*?</button>\s*(.*?)\s*<div class="collapse',
        re.DOTALL
    )

    # 2. Find the start of the links section
    links_start_pattern = re.compile(
        r'<div class="collapse navbar-collapse[^>]*id="navbarNav"[^>]*>.*?<ul class="navbar-nav[^>]*>',
        re.DOTALL
    )

    # 3. Find the center logo swap section and the second ul opening that splits the links
    center_logo_split_pattern = re.compile(
        r'</ul>\s*<!-- Center: Logo hover swap -->.*?</a>\s*<!-- Right Links \(3\) -->\s*<ul class="navbar-nav[^>]*>',
        re.DOTALL
    )

    count = 0
    for filename in os.listdir(directory):
        if not filename.endswith('.html'):
            continue
            
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if it has a navbar
        if '<nav class="navbar' not in content:
            continue
            
        # Check if it already looks updated (has our new class)
        if 'gap-lg-3 align-items-center"' in content:
            print(f"Skipping {filename} - Already looks updated")
            continue

        original_content = content

        # Step 1: Replace split ul lists with a single one by removing the center logo
        content = center_logo_split_pattern.sub('', content)

        # Step 2: Update the links wrapper opening
        content = links_start_pattern.sub(new_nav_links_open, content)

        # Step 3: Replace old mobile logo with new combined logo
        # We need to find the <a class="navbar-brand...> block specifically
        brand_block_pattern = re.compile(
            r'<!-- Mobile Logo -->\s*<a class="navbar-brand.*?</a>',
            re.DOTALL
        )
        content = brand_block_pattern.sub(new_nav_left, content)
        
        # Step 4: Fix Flexbox on pill container
        pill_container_pattern = re.compile(
            r'<div class="container pill-container">'
        )
        content = pill_container_pattern.sub(r'<div class="container pill-container d-flex justify-content-between align-items-center">', content)


        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            count += 1
            print(f"Updated {filename}")

    print(f"Successfully processed {count} files.")

if __name__ == "__main__":
    update_navbars(".")
