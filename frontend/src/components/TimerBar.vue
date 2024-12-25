<template>
    <section class="timerBar">
        <button @click="toggleButtons" class="timerButton" id="timerToggle"><img src="/images/timerToggle.svg"
                alt="Timer Options"></button>
        <button v-for="(time, index) in timerButtons" :key="index" class="timerButton">
            <img :src="time.src" :alt="time.alt">
        </button>
    </section>
</template>

<script>
function toggleButtons() {
    const buttons = document.querySelectorAll('.timerButton');
    buttons.forEach((button, index) => {
        setTimeout(() => {
            button.classList.toggle('shown');
        }, index * 50);
    });
}

export default {
    name: 'TimerBar',
    methods: {
        toggleButtons
    },
    data() {
        return {
            timerButtons: [
                { src: '/images/timer1.svg', alt: "1 Second" },
                { src: '/images/timer2.svg', alt: "2 Seconds" },
                { src: '/images/timer3.svg', alt: "3 Seconds" },
                { src: '/images/timer4.svg', alt: "4 Seconds" },
                { src: '/images/timer5.svg', alt: "5 Seconds" },
                { src: '/images/timerCustom.svg', alt: "Custom Timer" }
            ]
        };
    },
};
</script>

<style scoped>
.timerBar {
    display: flex;
    width: 100%;
    gap: .5rem;
}

.timerButton {
    display: flex;
    width: auto;
    height: 2.5rem;
    opacity: 0;
    user-select: none;
    pointer-events: none;
    transition: opacity 0.3s ease;
}

.timerButton:active {
    transform: scale(0.9);
}


.timerImg {
    width: auto;
    height: 100%;
}

.shown {
    opacity: 1;
    user-select: all;
    pointer-events: all;
}

#timerToggle {
    opacity: 1;
    user-select: all;
    pointer-events: all;
}


@media (min-width: 768px) {}
</style>