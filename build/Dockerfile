# Relinquishment — Docker build environment
# NOT TESTED — Docker not installed on current host
# Provides TeX Live 2025 for tagged PDF / PDF/A compliance

FROM texlive/texlive:TL2025-historic

# veraPDF for PDF/A validation
RUN apt-get update && apt-get install -y \
    wget \
    default-jre-headless \
    && rm -rf /var/lib/apt/lists/*

# Install veraPDF
RUN wget -q https://software.verapdf.org/releases/verapdf-installer.zip -O /tmp/verapdf.zip \
    && cd /tmp && unzip verapdf.zip \
    && cd verapdf-greenfield-* && ./verapdf-install --batch \
    && rm -rf /tmp/verapdf*

ENV LC_ALL=C
ENV TZ=UTC

WORKDIR /src

CMD ["make", "final"]
