const sections = [...document.querySelectorAll("main section[id]")];
const navLinks = [...document.querySelectorAll(".nav a")];

const sectionObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) {
        return;
      }

      navLinks.forEach((link) => {
        link.classList.toggle("active", link.hash === `#${entry.target.id}`);
      });
    });
  },
  { rootMargin: "-38% 0px -52% 0px", threshold: 0.01 }
);

sections.forEach((section) => sectionObserver.observe(section));

const heroVideo = document.querySelector(".video-hero-media");
const muteToggle = document.querySelector(".mute-toggle");

if (heroVideo) {
  const syncMuteToggle = () => {
    if (!muteToggle) {
      return;
    }

    muteToggle.textContent = heroVideo.muted ? "Sound" : "Mute";
    muteToggle.setAttribute("aria-pressed", String(heroVideo.muted));
    muteToggle.setAttribute(
      "aria-label",
      heroVideo.muted ? "Turn on background video sound" : "Mute background video"
    );
  };

  const playHeroVideo = () => {
    const playPromise = heroVideo.play();

    if (playPromise) {
      playPromise.catch(() => {
        heroVideo.controls = true;
      });
    }
  };

  if (muteToggle) {
    muteToggle.addEventListener("click", () => {
      heroVideo.muted = !heroVideo.muted;
      syncMuteToggle();
      playHeroVideo();
    });
  }

  window.addEventListener("load", () => {
    playHeroVideo();
  }, { once: true });

  syncMuteToggle();
}
