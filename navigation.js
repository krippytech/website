document.documentElement.classList.add("js");

document.addEventListener("DOMContentLoaded", () => {
    const dropdowns = [...document.querySelectorAll("[data-dropdown]")];
    const mobileToggle = document.querySelector(".mobile-menu-toggle");
    const mobilePanel = document.querySelector(".mobile-panel");
    let hoverCloseTimer;

    const closeDropdown = (group, restoreFocus = false) => {
        if (!group) {
            return;
        }

        group.classList.remove("is-open");
        delete group.dataset.openedByHover;

        const trigger = group.querySelector(".nav-trigger");
        trigger.setAttribute("aria-expanded", "false");

        if (restoreFocus) {
            trigger.focus();
        }
    };

    const closeAllDropdowns = (except = null) => {
        dropdowns.forEach((group) => {
            if (group !== except) {
                closeDropdown(group);
            }
        });
    };

    const openDropdown = (group, focusFirst = false, openedByHover = false) => {
        closeAllDropdowns(group);
        group.classList.add("is-open");

        if (openedByHover) {
            group.dataset.openedByHover = "true";
        } else {
            delete group.dataset.openedByHover;
        }

        const trigger = group.querySelector(".nav-trigger");
        trigger.setAttribute("aria-expanded", "true");

        if (focusFirst) {
            group.querySelector(".dropdown-menu a").focus();
        }
    };

    dropdowns.forEach((group) => {
        const trigger = group.querySelector(".nav-trigger");
        const links = [...group.querySelectorAll(".dropdown-menu a")];

        trigger.addEventListener("click", () => {
            if (group.dataset.openedByHover === "true") {
                delete group.dataset.openedByHover;
                return;
            }

            if (group.classList.contains("is-open")) {
                closeDropdown(group);
            } else {
                openDropdown(group);
            }
        });

        trigger.addEventListener("keydown", (event) => {
            if (event.key === "ArrowDown") {
                event.preventDefault();
                openDropdown(group, true);
            }

            if (event.key === "Escape") {
                event.preventDefault();
                closeDropdown(group, true);
            }
        });

        links.forEach((link, index) => {
            link.addEventListener("keydown", (event) => {
                if (event.key === "Escape") {
                    event.preventDefault();
                    closeDropdown(group, true);
                }

                if (event.key === "ArrowDown") {
                    event.preventDefault();
                    links[(index + 1) % links.length].focus();
                }

                if (event.key === "ArrowUp") {
                    event.preventDefault();
                    links[(index - 1 + links.length) % links.length].focus();
                }

                if (event.key === "Home") {
                    event.preventDefault();
                    links[0].focus();
                }

                if (event.key === "End") {
                    event.preventDefault();
                    links[links.length - 1].focus();
                }
            });
        });

        group.addEventListener("pointerenter", (event) => {
            if (event.pointerType === "mouse") {
                window.clearTimeout(hoverCloseTimer);
                openDropdown(group, false, true);
            }
        });

        group.addEventListener("pointerleave", (event) => {
            if (event.pointerType === "mouse") {
                hoverCloseTimer = window.setTimeout(() => closeDropdown(group), 140);
            }
        });

        group.addEventListener("focusout", (event) => {
            if (!group.contains(event.relatedTarget)) {
                closeDropdown(group);
            }
        });
    });

    if (mobileToggle && mobilePanel) {
        mobileToggle.addEventListener("click", () => {
            const willOpen = !mobilePanel.classList.contains("is-open");

            mobilePanel.classList.toggle("is-open", willOpen);
            mobileToggle.setAttribute("aria-expanded", String(willOpen));
            mobileToggle.setAttribute(
                "aria-label",
                willOpen ? "Close navigation menu" : "Open navigation menu",
            );
            closeAllDropdowns();
        });
    }

    document.addEventListener("click", (event) => {
        if (!event.target.closest("[data-dropdown]")) {
            closeAllDropdowns();
        }

        if (
            mobileToggle &&
            mobilePanel &&
            !event.target.closest(".site-header") &&
            mobilePanel.classList.contains("is-open")
        ) {
            mobilePanel.classList.remove("is-open");
            mobileToggle.setAttribute("aria-expanded", "false");
            mobileToggle.setAttribute("aria-label", "Open navigation menu");
        }
    });

    document.addEventListener("keydown", (event) => {
        if (event.key !== "Escape") {
            return;
        }

        const openGroup = document.querySelector("[data-dropdown].is-open");
        if (openGroup) {
            event.preventDefault();
            closeDropdown(openGroup, true);
            return;
        }

        if (mobileToggle && mobilePanel && mobilePanel.classList.contains("is-open")) {
            event.preventDefault();
            mobilePanel.classList.remove("is-open");
            mobileToggle.setAttribute("aria-expanded", "false");
            mobileToggle.setAttribute("aria-label", "Open navigation menu");
            mobileToggle.focus();
        }
    });

    window.addEventListener("resize", () => {
        if (
            window.innerWidth > 840 &&
            mobileToggle &&
            mobilePanel &&
            mobilePanel.classList.contains("is-open")
        ) {
            mobilePanel.classList.remove("is-open");
            mobileToggle.setAttribute("aria-expanded", "false");
            mobileToggle.setAttribute("aria-label", "Open navigation menu");
        }
    });
});
