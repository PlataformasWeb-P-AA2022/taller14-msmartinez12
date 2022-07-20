<template>
    <div class="pt-5">
        <div v-if="propietario && propietario.length">
            <div class="card mb-3" v-for="Propietario of propietario" v-bind:key="Propietario.id">
                <div class="row no-gutters">
                    <div class="col-md-4">
                        <div class="card-body">
                            <h5 class="card-title">Nombre: {{ Propietario.nombre }}</h5>
                            <h5 class="card-text">Apellido: {{ Propietario.apellido }}</h5>
                            <br>
                            <router-link :to="{name: 'edit', params: { id: Propietario.id }}" class="btn btn-sm btn-primary">Editar</router-link>
                            <button class="btn btn-danger btn-sm ml-1" v-on:click="deletePropietario(Propietario)">Eliminar</button>
                        </div>
                    </div>
                    <div class="col-md-8">
                        <div class="card-body">
                            <p class="card-text">Cédula: {{ Propietario.cedula }}</p>
                            <p class="card-text">Correo: {{ Propietario.correo }}</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <p  v-if="propietario.length == 0"> Sin Propietarios</p>
    </div>
</template>
<script>

import axios from 'axios';

export default {
    data() {
        return {
            propietario: []
        }
    },
    created() {
        this.all();
    },
    methods: {
        deletePropietario: function(e) {
            if (confirm('Eliminar ' + e.nombre)) {
                axios.delete(e.url)
                    .then( response => {
                        this.all();
                    });
            }
        },
        all: function () {
            axios.get('http://127.0.0.1:8000/api/propietario/')
                .then( response => {
                    this.propietario = response.data
                });
        }
    },
}
</script>
