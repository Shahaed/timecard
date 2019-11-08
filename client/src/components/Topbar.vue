<template>
    <b-navbar>
        <template slot="brand">
            <b-navbar-item href="https://timecard.iseinc.biz/">
                <img
                    src="https://www.iseinc.biz/wp-content/uploads/2019/06/logo2.png"
                    alt="ISE"
                >
            </b-navbar-item>
        </template>
        <template slot="start">
        </template>

        <template slot="end">
            <b-navbar-item tag="div">
                <div class="buttons">
                    <a class="button is-danger">
                        <strong>Log out</strong>
                    </a>
                </div>
            </b-navbar-item>
        </template>
    </b-navbar>
</template>

<script>
export default {
    name: 'Topbar'
}
</script>
