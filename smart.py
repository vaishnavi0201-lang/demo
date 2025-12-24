import os
import re

# Root directory where all subprojects live
project_root = r"C:\Users\vaisnavi murugesan\.gemini\antigravity\scratch\stitch_3d_face_mapping_enrollment"

# Use a unique comment to track updates reliably
home_button_html = """
    <a href="../index.html" style="position: fixed; top: 20px; left: 20px; z-index: 9999; background: #111827; color: white; padding: 10px 20px; border-radius: 999px; text-decoration: none; font-family: sans-serif; font-weight: 600; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06); border: 1px solid rgba(255,255,255,0.1); display: flex; align-items: center; gap: 8px; transition: all 0.2s;" onmouseenter="this.style.transform='translateY(-2px)';this.style.boxShadow='0 10px 15px -3px rgba(0, 0, 0, 0.5)';" onmouseleave="this.style.transform='translateY(0)';this.style.boxShadow='0 4px 6px -1px rgba(0, 0, 0, 0.1)';">
        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>
        <span>Dashboard</span>
    </a>
"""

subprojects = [
    "3d_face_mapping_enrollment",
    "ai-powered_leave_concierge",
    "anomaly_security_audit_trail",
    "command_center_real-time_map",
    "dynamic_qr_&_nfc_wallet_card",
    "geofence_perimeter_configurator",
    "holographic_authentication_gateway",
    "liveness_live-feed_dashboard",
    "payroll-ready_export_engine",
    "time-flow_personal_analytics"
]

def update_html_files():
    for folder in subprojects:
        file_path = os.path.join(project_root, folder, "index.html")
        
        if not os.path.exists(file_path):
            print(f"Skipping: {folder} (File not found at {file_path})")
            continue

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            # FIX: Check for the unique comment instead of an empty string
            if "" in content:
                print(f"Already updated: {folder}")
                continue

            # Case-insensitive body tag search to handle <body class="..."> etc.
            body_match = re.search(r"<body[^>]*>", content, re.IGNORECASE)

            if body_match:
                end_pos = body_match.end()
                # Injecting newline for cleaner HTML source code
                new_content = content[:end_pos] + "\n" + home_button_html + content[end_pos:]
                
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"Successfully injected: {folder}")
            else:
                print(f"Error: No <body> tag found in {folder}")

        except Exception as e:
            print(f"Failed to process {folder}: {e}")

if __name__ == "__main__":
    update_html_files()